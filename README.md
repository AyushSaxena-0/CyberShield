# 🛡️ CyberShield

### AI-Powered Cybersecurity Intelligence Platform

CyberShield is an AI-driven cybersecurity solution designed to identify malicious URLs, analyze suspicious activities, and provide intelligent threat detection using Machine Learning.

The platform helps users verify website safety before visiting them, reducing exposure to phishing attacks, fraudulent websites, and other cyber threats.

Trusted Link
<img width="1918" height="863" alt="image" src="https://github.com/user-attachments/assets/1b23dfb1-e1be-4ce1-84aa-50012fe4b5a5" />

Fake Link
<img width="1896" height="863" alt="image" src="https://github.com/user-attachments/assets/ef42e50c-0391-4ba6-98c0-8441347ccc28" />





---

## 🚀 Features

### 🔍 Malicious URL Detection

* Detects phishing and suspicious URLs using Machine Learning.
* Real-time prediction with confidence scores.
* Fast response suitable for security workflows.

### 🧠 AI-Based Threat Analysis

* Uses trained machine learning models to identify patterns associated with malicious websites.
* Learns from large datasets of legitimate and phishing URLs.

### 🌍 Geo-Location Intelligence

* Integrates GeoLite2 database for location-based threat analysis.
* Helps identify suspicious hosting regions.

### 📊 Threat Scoring

* Generates risk scores for URLs.
* Categorizes websites into:

  * Safe
  * Suspicious
  * Malicious

### 🖥️ User-Friendly Interface

* Simple graphical interface for URL analysis.
* Designed for both technical and non-technical users.

---

## 🏗️ System Architecture

```text
User Input URL
       │
       ▼
Feature Extraction
       │
       ▼
Machine Learning Model
       │
       ▼
Threat Classification
       │
       ▼
Risk Assessment & Result
```

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Machine Learning

* Scikit-Learn
* Pandas
* NumPy

### Cybersecurity

* Threat Intelligence Datasets
* URL Feature Engineering
* GeoLite2

### Interface

* Tkinter / Python GUI

---

## 📂 Project Structure

```text
CyberShield/
│
├── api.py                  # Backend APIs
├── ui.py                   # User Interface
├── train.py                # Model Training Script
├── threat_model.pkl        # Trained ML Model
├── phishing_site_urls.csv  # Training Dataset
├── GeoLite2-City.mmdb      # Geo-location Database
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/AyushSaxena-0/CyberShield.git
cd CyberShield
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python ui.py
```

---

## 🧪 Model Training

To retrain the phishing detection model:

```bash
python train.py
```

The newly trained model will be saved as:

```text
threat_model.pkl
```

---

## 📈 Future Enhancements

* Deepfake Detection Module
* Fake News Verification Engine
* Real-Time Threat Intelligence Feeds
* Browser Extension
* Email Phishing Scanner
* RAG-Based Cybersecurity Assistant
* AI Security Copilot

---

## 🎯 Use Cases

* Personal Cyber Safety
* Enterprise Security Monitoring
* Educational Cybersecurity Labs
* Threat Research
* Security Awareness Programs

---

## 👨‍💻 Developer

**Ayush Saxena**

AI Engineer | Machine Learning Enthusiast | Cybersecurity Innovator

Focused on building intelligent systems that combine Artificial Intelligence with real-world cybersecurity solutions.
Linked In www.linkedin.com/in/ayush-saxena-b29912241

---

## 📜 License

This project is intended for educational and research purposes.
## ⚠️ Disclaimer & Model Accuracy

CyberShield is an AI-assisted cybersecurity tool designed to help identify potentially malicious URLs. While the system has been trained on large phishing datasets and achieves approximately **90% accuracy** on the evaluation dataset, it is not perfect and should not be considered a substitute for professional cybersecurity solutions.

### 📊 Model Performance

| Metric   | Score                |
| -------- | -------------------- |
| Accuracy | **90.0%**            |
| Status   | Production Prototype |

### Important Limitations

* False positives may occur, causing legitimate websites to be flagged as suspicious.
* False negatives may occur, allowing some malicious URLs to be classified as safe.
* New phishing techniques and zero-day threats may not always be detected.
* Predictions should be used as guidance and not as the sole basis for security decisions.

### Security Notice

CyberShield should be used alongside antivirus software, browser security protections, threat intelligence services, and manual verification practices.

**The developer does not guarantee 100% threat detection accuracy and assumes no liability for damages resulting from the use of this software.**

Use responsibly and ethically.

```
```
