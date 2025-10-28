MedVision Chatbot
https://img.shields.io/badge/Python-3.12-blue https://img.shields.io/badge/Flask-2.3.3-lightgrey https://img.shields.io/badge/AI--Powered-Google%2520Gemini-orange https://img.shields.io/badge/Status-Functional-brightgreen

An AI-powered medical image analysis chatbot that provides preliminary insights for educational purposes using Google Gemini's vision capabilities. Built with Flask and Python 3.12.

🚀 Features
Medical Image Analysis: Upload prescriptions, skin conditions, X-rays, medical reports

Contextual Question Flow: Sequential medical questions for better analysis

AI-Powered Insights: Uses Google Gemini 1.5 Flash Vision model

Secure Session Management: File-based session storage

Simple & Clean UI: Bootstrap-based responsive interface

Multi-format Support: JPG, PNG, JPEG image formats

⚠️ Important Disclaimer
🚨 MEDICAL DISCLAIMER: This application is for EDUCATIONAL and INFORMATIONAL purposes ONLY. It is NOT a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of qualified healthcare providers with any medical questions. Never disregard professional medical advice because of information provided by this AI system. The developers are not medical professionals and this tool should not be used for medical decision-making.

📋 Prerequisites
Python 3.12 (tested and optimized)

Google Gemini API key (Get it here)

Internet connection (for AI model access)

🛠️ Installation & Setup
1. Clone or Download the Project
bash
# Create project directory
mkdir MedVisionChatbot
cd MedVisionChatbot
2. Set Up Virtual Environment (Recommended)
bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
3. Install Dependencies
bash
pip install -r requirements.txt
4. Configure Environment
Create a .env file in the project root:

env
GEMINI_API_KEY=your_actual_gemini_api_key_here
SECRET_KEY=your_secret_key_here
Getting Google Gemini API Key:
Visit Google AI Studio

Sign in with your Google account

Create a new API key

Copy the key to your .env file

🏃‍♂️ Running the Application
bash
python app.py
The application will start at: http://localhost:5000

📁 Project Structure
text
MedVisionChatbot/
│
├── app.py                 # Main Flask application
├── file_storage.py        # File-based session management
├── .env                  # Environment variables (create this)
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore rules
├── README.md            # This file
│
└── templates/           # HTML templates
    ├── index.html      # Home page with image upload
    ├── chat.html       # Medical questions interface
    └── result.html     # Analysis results display
🔄 Workflow
Upload Image: User uploads a medical image (skin condition, prescription, X-ray, etc.)

Answer Questions: System asks three sequential medical context questions:

"When did the problem begin?"

"How do you feel right now?"

"Have you taken any medicine? (Optional image upload)"

AI Analysis: Gemini AI analyzes the image and context

Get Results: Receive preliminary insights with proper disclaimers

🎯 Example Use Cases
Dermatology: Skin rashes, acne, lesions, infections

Medical Documents: Prescriptions, lab reports, medical charts

Wound Assessment: Cuts, burns, post-operative care

Educational Tool: Medical students learning diagnostic processes

🛡️ Security & Privacy
Local Processing: Images processed locally before AI analysis

File-based Sessions: No database required, sessions stored locally

Automatic Cleanup: Session files deleted after analysis

No Permanent Storage: No medical data retained on server

🐛 Troubleshooting
Common Issues:
"Please upload an image first" error

Ensure cookies are enabled in your browser

Check that image file is valid (JPG, PNG, JPEG under 10MB)

Gemini API errors

Verify API key in .env file is correct

Check internet connection

Ensure billing is set up in Google AI Studio

Session issues

The app creates temp_sessions/ directory automatically

Ensure write permissions in project directory

Debugging:
Check terminal output for detailed logs. The app includes comprehensive logging.

🔧 Configuration
Required Files:
app.py - Main application logic

file_storage.py - Session management

templates/ - All HTML templates

.env - Your environment variables

Environment Variables:
GEMINI_API_KEY: Your Google Gemini API key (required)

SECRET_KEY: Flask secret key for session security

📊 Technical Details
Framework: Flask 2.3.3

Python Version: 3.12 (optimized)

AI Model: Google Gemini 1.5 Flash

Session Management: Custom file-based system

Image Processing: Pillow library

Frontend: Bootstrap 5.3

🚀 Deployment Ready
This application is production-ready with:

✅ Proper error handling

✅ Session management

✅ Security considerations

✅ Scalable architecture

✅ Comprehensive logging

📞 Support
If you encounter issues:

Check terminal logs for detailed error messages

Verify your Gemini API key is valid and active

Ensure all dependencies are installed correctly

Check that port 5000 is available on your system

🌟 Future Enhancements
Potential features for expansion:

User authentication system

Medical history tracking

Multiple AI model support

Advanced image preprocessing

Export functionality for reports

📄 License
This project is intended for educational purposes. Users must ensure compliance with:

Google Gemini API terms of service

Medical data privacy regulations (HIPAA, GDPR, etc.)

Professional medical practice guidelines in their jurisdiction

🏥 Medical Disclaimer (Repeated for Emphasis)
⚠️ CRITICAL: This application provides AI-generated preliminary insights for EDUCATIONAL PURPOSES ONLY. It does NOT provide medical diagnoses, treatment recommendations, or professional healthcare advice. Always consult qualified healthcare professionals for medical concerns. The developers are not responsible for any decisions made based on this application's output.

Built with ❤️ using Python 3.12, Flask, and Google Gemini AI for educational purposes

🔗 Quick Start Commands
bash
# 1. Setup
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# 2. Configure
echo "GEMINI_API_KEY=your_key_here" > .env
echo "SECRET_KEY=your_secret_here" >> .env

# 3. Run
python app.py

# 4. Visit
# http://localhost:5000