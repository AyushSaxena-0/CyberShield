from fastapi import FastAPI
from pydantic import BaseModel
import whois
import geoip2.database
from datetime import datetime
import ollama
import socket

app = FastAPI()

# Ensure GeoLite2-City.mmdb is in the same folder as api.py
# Use the absolute path if it still throws a FileNotFoundError
reader = geoip2.database.Reader('GeoLite2-City.mmdb')


class URLRequest(BaseModel):
    url: str


def get_forensic_data(domain):
    """Compiles real-time domain age and physical hosting location."""
    # 1. WHOIS Age
    try:
        w = whois.whois(domain)
        creation_date = w.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        age = (datetime.now() - creation_date).days if creation_date else 3650
    except:
        age = 3650

    # 2. Geolocation
    try:
        ip = socket.gethostbyname(domain)
        response = reader.city(ip)
        location = f"{response.country.name}, {response.city.name}"
    except:
        location = "Unknown/Hidden"
    return age, location


@app.post("/api/v1/analyze/url")
def analyze_url(request: URLRequest):
    url = request.url
    domain = url.split('/')[2] if len(url.split('/')) > 2 else url

    age, location = get_forensic_data(domain)

    # LLM Forensic Compilation
    prompt = f"Analyze domain: {domain}. Age: {age} days. Location: {location}. Is this a phishing attempt? Respond 'CRITICAL THREAT' or 'SECURE' followed by a brief forensic reason."

    try:
        llm_resp = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])
        reasoning = llm_resp['message']['content']
    except:
        reasoning = "Forensic analysis engine offline."

    # Binary Classification based on LLM response
    is_threat = "CRITICAL THREAT" in reasoning.upper()

    return {
        "classification": "CRITICAL THREAT" if is_threat else "SECURE",
        "reasons": [reasoning, f"Hosting Location: {location}"]
    }