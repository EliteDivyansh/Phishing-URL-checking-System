# Phishing-URL-checking-System
A simple Flask-based web app that detects phishing URLs using rule-based checks. It analyzes URL patterns, HTTPS usage, shorteners, keywords, and subdomains to estimate safety — no machine learning required. Lightweight, fast, and perfect for cybersecurity demos or college projects.

# 🧠 Phishing URL Detection (Rule-Based)

A simple web application built with **Flask** that detects potentially **phishing URLs** using basic rule-based checks — no machine learning required.

## 🚀 Features
- Detects suspicious URLs using simple pattern rules:
  - Presence of IP address instead of domain  
  - Missing HTTPS  
  - Shortened URLs (e.g., bit.ly, tinyurl)  
  - Suspicious keywords like `login`, `verify`, `secure`, etc.  
  - Excessive subdomains or very long URLs  
- Lightweight (just Flask + pure Python)
- Interactive web UI built with Bootstrap 5
- Works locally — no internet connection or API required

## 🧰 Tech Stack
- **Python 3.x**
- **Flask 2.2.5**
- **HTML, CSS, JavaScript (Bootstrap)**

## 🖥️ Installation & Run
1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/phishing-url-detector.git
   cd phishing-url-detector
🧑‍💻 Author

Divyansh Sharma

Made as a simple cybersecurity demo project using Flask 🚀
