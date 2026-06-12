import os
import zipfile
import pandas as pd
import joblib
import math
from difflib import SequenceMatcher
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# --- 1. DOWNLOAD & UNZIP FROM KAGGLE ---
DATASET_NAME = "taruntiwarihp/phishing-site-urls"
ZIP_FILE = "phishing-site-urls.zip"
CSV_FILE = "phishing_site_urls.csv"

# It will only download if you don't already have the CSV!
if not os.path.exists(CSV_FILE):
    print("Downloading massive dataset from Kaggle...")
    os.system(f"python -m kaggle datasets download -d {DATASET_NAME}")

    print("Unzipping payload...")
    with zipfile.ZipFile(ZIP_FILE, 'r') as zip_ref:
        zip_ref.extractall()
    print("Unzip complete!")

# --- 2. LOAD DATA ---
print("Loading data into Pandas...")
df = pd.read_csv(CSV_FILE)

# Sample 50,000 rows so your computer doesn't catch fire.
# (You can remove this line later if you want to train on all 549k rows over night)
df = df.sample(n=50000, random_state=42)

# --- 3. MATHEMATICAL FEATURE EXTRACTION ---
print("Extracting threat vectors... (Grab a coffee, this takes a minute!)")

TARGET_BRANDS = ["flipkart", "amazon", "paypal", "google", "apple", "microsoft", "netflix", "bank"]


def calculate_entropy(text):
    if not text: return 0
    entropy = 0
    for x in set(text):
        p_x = float(text.count(x)) / len(text)
        entropy += - p_x * math.log(p_x, 2)
    return round(entropy, 2)


def is_typosquat(url):
    url_lower = str(url).lower()
    for brand in TARGET_BRANDS:
        if brand not in url_lower:
            for word in url_lower.replace('.', ' ').replace('-', ' ').split():
                similarity = SequenceMatcher(None, brand, word).ratio()
                if 0.8 < similarity < 1.0:
                    return 1
    return 0


def extract_features(url):
    url_str = str(url)
    num_dots = url_str.count('.')
    entropy = calculate_entropy(url_str)
    sus_count = sum(
        1 for w in ["login", "verify", "secure", "update", "free", "admin", "account"] if w in url_str.lower())
    typosquat_flag = is_typosquat(url_str)
    return [len(url_str), num_dots, entropy, sus_count, typosquat_flag]


# Process the data
features = list(df['URL'].apply(extract_features))
# The dataset labels are 'bad' and 'good'. We convert them to 1 and 0.
labels = df['Label'].apply(lambda x: 1 if x == 'bad' else 0)

# --- 4. TRAIN THE NEURAL ENGINE ---
print("Training the Random Forest Classifier...")
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# n_jobs=-1 tells the AI to use all of your CPU cores to train faster!
model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

# Evaluate the AI
accuracy = model.score(X_test, y_test)
print(f"=====================================")
print(f"🎯 Model Accuracy: {accuracy * 100:.2f}%")
print(f"=====================================")

# --- 5. SAVE THE BRAIN ---
joblib.dump(model, 'threat_model.pkl')
print("Production-grade model successfully saved as threat_model.pkl!")