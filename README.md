# 🩺 MedVision Chatbot

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.3-lightgrey)
![AI-Powered](https://img.shields.io/badge/AI--Powered-Google%20Gemini-orange)
![Status](https://img.shields.io/badge/Status-Functional-brightgreen)

An **AI-powered medical image analysis chatbot** that provides **preliminary insights for educational purposes** using **Google Gemini’s vision capabilities**.  
Built with **Flask** and **Python 3.12**.

---

## 🚀 Features

- **Medical Image Analysis:** Upload prescriptions, skin conditions, X-rays, or reports  
- **Contextual Question Flow:** Sequential medical questions for better insights  
- **AI-Powered Insights:** Google Gemini 1.5 Flash Vision model  
- **Secure Session Management:** File-based storage  
- **Responsive UI:** Bootstrap-based clean interface  
- **Multi-format Support:** JPG, PNG, JPEG image formats  

---

## ⚠️ Important Disclaimer

> 🚨 **MEDICAL DISCLAIMER:**  
> This application is for **EDUCATIONAL and INFORMATIONAL purposes only**.  
> It is **NOT a substitute for professional medical advice, diagnosis, or treatment**.  
> Always seek the advice of qualified healthcare providers for medical concerns.  
> The developers are not medical professionals — this tool should **not** be used for real medical decision-making.

---

## 📋 Prerequisites

- **Python 3.12** (tested and optimized)  
- **Google Gemini API Key** – [Get it here](https://makersuite.google.com/app/apikey)  
- **Internet connection** for AI access  

---

## 🛠️ Installation & Setup

### 1️⃣ Clone or Download the Project
```bash
# Create project directory
mkdir MedVisionChatbot
cd MedVisionChatbot
2️⃣ Set Up Virtual Environment
bash
Copy code
# Create virtual environment
python -m venv venv

# Activate environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Configure Environment
Create a .env file in your project root:

env
Copy code
GEMINI_API_KEY=your_actual_gemini_api_key_here
SECRET_KEY=your_secret_key_here
Getting the Google Gemini API key:

Visit Google AI Studio

Sign in with your Google account

Create a new API key

Copy it to your .env file

🏃 Running the Application
bash
Copy code
python app.py
Access it at 👉 http://localhost:5000

📁 Project Structure
bash
Copy code
MedVisionChatbot/
│
├── app.py                # Main Flask app
├── file_storage.py       # File-based session management
├── .env                  # Environment variables
├── requirements.txt      # Dependencies
├── .gitignore
├── README.md
│
└── templates/
    ├── index.html        # Home page (upload)
    ├── chat.html         # Question flow
    └── result.html       # AI-generated results
🔄 Workflow
Upload Image: (skin, prescription, X-ray, etc.)

Answer Questions:

When did the problem begin?

How do you feel right now?

Have you taken any medicine?

AI Analysis: Gemini analyzes image + context

Get Results: Receive AI-generated preliminary insights with disclaimers

🎯 Example Use Cases
Dermatology: rashes, acne, infections

Medical documents: prescriptions, reports

Wound assessment: cuts, burns, post-surgery

Educational use: medical students & AI demos

🛡️ Security & Privacy
Local Processing: Images handled locally before AI call

File-based Sessions: No database required

Automatic Cleanup: Temp files auto-deleted

No Permanent Storage: No user data retained

🐛 Troubleshooting
Common Issues:

“Please upload an image first” → ensure cookies enabled + valid file

Gemini API error → verify .env key + internet + billing setup

Session error → check write permission in temp_sessions/

Debugging:
Check terminal logs — detailed output is provided.

🔧 Configuration Summary
File	Purpose
app.py	Main Flask logic
file_storage.py	Session handling
templates/	HTML templates
.env	API keys and secrets

Environment Variables

GEMINI_API_KEY → your Google Gemini key

SECRET_KEY → Flask secret

📊 Technical Details
Component	Version / Info
Framework	Flask 2.3.3
Python	3.12
AI Model	Google Gemini 1.5 Flash
Session	File-based
Frontend	Bootstrap 5.3
Image Handling	Pillow

🚀 Deployment Ready
✅ Error handling
✅ Secure sessions
✅ Logging
✅ Scalable
✅ Lightweight

📞 Support
If you encounter issues:

Check terminal logs

Verify Gemini API key

Ensure dependencies installed

Make sure port 5000 is free

🌟 Future Enhancements
User authentication

Medical history tracking

Multi-model support

Advanced preprocessing

Exportable reports

📄 License
This project is for educational use.
Ensure compliance with:

Google Gemini API Terms of Service

Data privacy laws (HIPAA, GDPR, etc.)

Local medical guidelines

🏥 Medical Disclaimer (Reiterated)
⚠️ This app provides AI-generated insights for educational purposes only.
It is not medical advice, not diagnostic, and should never replace professional healthcare consultation.
The developers assume no liability for any misuse.

💡 Quick Start Commands
bash
Copy code
# 1. Setup
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# 2. Configure
echo "GEMINI_API_KEY=your_key_here" > .env
echo "SECRET_KEY=your_secret_here" >> .env

# 3. Run
python app.py

# 4. Visit
# http://localhost:5000
Built with ❤️ using Python 3.12, Flask, and Google Gemini AI for educational purposes.