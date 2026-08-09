
# 🛡️ Phishing Detection System

### AI-Powered Multi-Channel Threat Detection — URLs • Emails • SMS

**A machine learning-based cybersecurity system that detects phishing attempts across URLs, emails, and SMS messages — in real time.**

[Features](#-features) • [Architecture](#-architecture) • [Installation](#-installation) • [Usage](#-usage) • [Tech Stack](#-tech-stack) • [Contributing](#-contributing)

---

## 📖 Overview

Phishing attacks remain one of the most common and dangerous cybersecurity threats — targeting individuals and organizations through deceptive **links, emails, and text messages**. This project combines **machine learning** with **cybersecurity heuristics** to automatically analyze suspicious content and classify it as **legitimate** or **potentially malicious**, helping users identify threats before they cause harm.

Unlike single-purpose detectors, this system is built as a **unified, multi-vector defense platform** — covering the three most common phishing attack surfaces in one dashboard.

---

## ✨ Features

| Module | Description |
|---|---|
| 🔗 **URL Analyzer** | Detects malicious/spoofed URLs using pattern analysis and ML classification |
| 📧 **Email Scanner** | Flags phishing emails based on content, headers, and linguistic patterns |
| 📱 **SMS Detector** | Identifies smishing (SMS phishing) attempts in text messages |
| 📊 **Interactive Dashboard** | Centralized view to monitor scans, results, and threat statistics |
| 🧠 **ML-Powered Classification** | Dedicated trained models for each channel (URL, Email, SMS) |
| 🩹 **Recovery Guidance** | Step-by-step guidance page for users who may have already been compromised |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                      Web Interface                       │
│   home.html │ dashboard.html │ url.html │ email.html      │
│                      │ sms.html │ recovery.html            │
└──────────────────────────┬────────────────────────────────┘
                            │
                     ┌──────▼──────┐
                     │   app.py    │  ◄── Flask Backend
                     │  (Routing)  │
                     └──────┬──────┘
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
┌───────────────┐  ┌────────────────┐  ┌────────────────┐
│url_ml_model.py│  │email_ml_model.py│  │sms_ml_model.py │
│  (URL Model)  │  │  (Email Model)  │  │  (SMS Model)   │
└───────────────┘  └─────────────────┘  └────────────────┘
        │                   │                   │
        └───────────────────┼───────────────────┘
                            ▼
                    ┌───────────────┐
                    │  Features.py  │  ◄── Feature Extraction
                    └───────────────┘
```

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Machine Learning:** Scikit-learn (classification models trained per channel)
- **Frontend:** HTML, CSS, JavaScript
- **Feature Engineering:** Custom feature extraction pipeline (`Features.py`)

---

## 📂 Project Structure

```
Phishing-Detection-System/
│
├── app.py                  # Main Flask application & routes
├── Features.py              # Feature extraction utilities for ML models
│
├── url_ml_model.py          # URL phishing classification model
├── email_ml_model.py        # Email phishing classification model
├── sms_ml_model.py          # SMS phishing classification model
│
├── home.html                 # Landing page
├── dashboard.html             # Analytics & results dashboard
├── url.html                  # URL scanner interface
├── email.html                 # Email scanner interface
├── sms.html                   # SMS scanner interface
├── recovery.html               # Post-attack recovery guidance
│
└── README.md
```

---

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/Yash-world/Phishing-Detection-System.git
cd Phishing-Detection-System

# 2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
python app.py
```

The app will start on `http://127.0.0.1:5000/` — open it in your browser to access the dashboard.

---

## 🚀 Usage

1. Launch the app and open the **Home** page.
2. Choose a scan type — **URL**, **Email**, or **SMS**.
3. Paste the content you want to analyze.
4. The system extracts features and runs it through the relevant trained ML model.
5. Get instant results and threat statistics on the **Dashboard**: ✅ **Legitimate** or 🚨 **Phishing Detected**.
6. If flagged, refer to the **Recovery** page for suggested next steps.

---

## 🗺️ Roadmap

- [ ] Add REST API endpoints for programmatic access
- [ ] Browser extension for real-time URL scanning
- [ ] Model performance metrics dashboard (precision/recall/F1)
- [ ] Support for additional languages in SMS/email detection
- [ ] Dockerize the application for easier deployment

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 👤 Author

**Yash-world**
GitHub: [@Yash-world](https://github.com/Yash-world)

