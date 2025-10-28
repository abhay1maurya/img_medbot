from flask import Flask, render_template, request, session, redirect, url_for, flash, make_response
import google.generativeai as genai
from PIL import Image
import os
from dotenv import load_dotenv
import io
import base64
import secrets
from file_storage import storage

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', secrets.token_hex(16))

# Configure Gemini
try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    gemini_configured = True
    print("✅ Gemini AI configured successfully")
except Exception as e:
    print(f"❌ Gemini configuration failed: {e}")
    gemini_configured = False

def get_or_create_session(request):
    """Get existing session ID from cookie or create new one"""
    session_id = request.cookies.get('medvision_session')
    if not session_id:
        session_id = storage.create_session()
        print(f"🆕 Created new session: {session_id}")
    else:
        print(f"📁 Using existing session: {session_id}")
    return session_id

@app.route('/')
def home():
    session_id = get_or_create_session(request)
    session_data = storage.load_session(session_id)
    
    response = make_response(render_template('index.html'))
    response.set_cookie('medvision_session', session_id, max_age=3600)  # 1 hour
    return response

@app.route('/upload', methods=['POST'])
def upload_image():
    print("📤 Upload endpoint called")
    
    session_id = get_or_create_session(request)
    
    if 'image' not in request.files:
        flash('Please select an image file.', 'error')
        return redirect(url_for('home'))
    
    file = request.files['image']
    if file.filename == '':
        flash('No file selected.', 'error')
        return redirect(url_for('home'))
    
    try:
        # Verify it's an image
        image = Image.open(file.stream)
        image.verify()
        
        # Reset stream position and read image data
        file.stream.seek(0)
        image_data = file.read()
        
        # Load existing session data or create new
        session_data = storage.load_session(session_id) or {}
        
        # Update session data
        session_data['uploaded_image'] = base64.b64encode(image_data).decode('utf-8')
        session_data['current_question'] = 1
        session_data['answers'] = {}
        
        # Save session
        storage.save_session(session_id, session_data)
        
        print(f"✅ Image uploaded successfully. Session: {session_id}")
        print(f"📊 Session data keys: {list(session_data.keys())}")
        
        # Redirect to chat with session cookie
        response = make_response(redirect(url_for('chat')))
        response.set_cookie('medvision_session', session_id, max_age=3600)
        return response
        
    except Exception as e:
        print(f"❌ Image upload error: {e}")
        flash('Invalid image file. Please upload JPG, PNG, or JPEG.', 'error')
        return redirect(url_for('home'))

@app.route('/chat')
def chat():
    session_id = request.cookies.get('medvision_session')
    
    if not session_id:
        print("❌ No session ID in cookie")
        flash('Please upload an image first.', 'error')
        return redirect(url_for('home'))
    
    session_data = storage.load_session(session_id)
    print(f"💬 Chat endpoint - Session ID: {session_id}")
    print(f"📊 Session data: {session_data}")
    
    if not session_data or not session_data.get('uploaded_image'):
        print("❌ No image data in session")
        flash('Please upload an image first.', 'error')
        return redirect(url_for('home'))
    
    current_question = session_data.get('current_question', 1)
    questions = {
        1: "When did the problem begin?",
        2: "How do you feel right now?",
        3: "Have you taken any medicine for this problem? If yes, please show a picture of the bottle or box."
    }
    
    print(f"💬 Showing question {current_question}")
    return render_template('chat.html', 
                         question=questions[current_question],
                         question_number=current_question,
                         total_questions=len(questions))

@app.route('/answer', methods=['POST'])
def process_answer():
    session_id = request.cookies.get('medvision_session')
    
    if not session_id:
        flash('Please upload an image first.', 'error')
        return redirect(url_for('home'))
    
    session_data = storage.load_session(session_id)
    
    print("📝 Answer endpoint called")
    
    if not session_data or not session_data.get('uploaded_image'):
        flash('Please upload an image first.', 'error')
        return redirect(url_for('home'))
    
    current_question = session_data.get('current_question', 1)
    
    # Get text answer
    text_answer = request.form.get('text_answer', '').strip()
    print(f"📄 Text answer for Q{current_question}: {text_answer}")
    
    # Handle image answer
    image_answer = None
    if 'image_answer' in request.files:
        file = request.files['image_answer']
        if file and file.filename != '':
            try:
                image = Image.open(file.stream)
                image.verify()
                file.stream.seek(0)
                image_data = file.read()
                image_answer = base64.b64encode(image_data).decode('utf-8')
                print("🖼️ Image answer uploaded")
            except Exception as e:
                print(f"⚠️ Medicine image error: {e}")
    
    # Validate answer
    if not text_answer and not image_answer:
        flash('Please provide an answer before continuing.', 'warning')
        return redirect(url_for('chat'))
    
    # Ensure answers dict exists
    if 'answers' not in session_data:
        session_data['answers'] = {}
    
    # Store answer
    session_data['answers'][f'question_{current_question}'] = {
        'text': text_answer,
        'image': image_answer
    }
    
    # Move to next question or analyze
    if current_question < 3:
        session_data['current_question'] = current_question + 1
        storage.save_session(session_id, session_data)
        print(f"➡️ Moving to question {current_question + 1}")
        return redirect(url_for('chat'))
    else:
        storage.save_session(session_id, session_data)
        print("🔍 All questions answered, proceeding to analysis")
        return redirect(url_for('analyze'))

@app.route('/analyze')
def analyze():
    session_id = request.cookies.get('medvision_session')
    
    if not session_id:
        flash('Please complete the question process first.', 'error')
        return redirect(url_for('home'))
    
    session_data = storage.load_session(session_id)
    
    print("🔬 Analysis endpoint called")
    
    if not session_data or not session_data.get('uploaded_image') or not session_data.get('answers'):
        flash('Please complete the question process first.', 'error')
        return redirect(url_for('home'))
    
    try:
        if not gemini_configured:
            result = "⚠️ AI service is currently unavailable. Please try again later."
        else:
            # Reconstruct image
            image_data = base64.b64decode(session_data['uploaded_image'])
            image = Image.open(io.BytesIO(image_data))
            
            # Get answers
            answers = session_data['answers']
            answer_1 = answers.get('question_1', {}).get('text', 'No answer provided')
            answer_2 = answers.get('question_2', {}).get('text', 'No answer provided')
            answer_3 = answers.get('question_3', {}).get('text', 'No answer provided')
            
            print(f"📋 Answers: Q1={answer_1}, Q2={answer_2}, Q3={answer_3}")
            
            # Prepare prompt
            prompt = f"""
            Analyze this medical image and provide preliminary insights in 10 points not more than 10 words in a line.

            User Context:
            1. Problem began: {answer_1}
            2. Current feelings: {answer_2}
            3. Medications taken: {answer_3}

            Please provide:
            - What the image might show
            - Possible conditions to consider
            - Recommended next steps
            - When to seek immediate care

            Remember: This is not a diagnosis. Be professional and empathetic.
            Always recommend consulting healthcare professionals.
            """
            
            # Generate analysis
            model = genai.GenerativeModel("gemini-2.0-flash")
            response = model.generate_content([prompt, image])
            result = response.text
            
            print("✅ Analysis completed successfully")
        
    except Exception as e:
        print(f"❌ Analysis error: {e}")
        result = f"Sorry, there was an error processing your request. Please try again."
    
    # Clean up session after analysis
    storage.delete_session(session_id)
    
    response = make_response(render_template("result.html", result=result))
    response.set_cookie('medvision_session', '', expires=0)
    return response

@app.route('/restart')
def restart():
    session_id = request.cookies.get('medvision_session')
    if session_id:
        storage.delete_session(session_id)
    
    flash('Session cleared. You can start a new analysis.', 'info')
    
    response = make_response(redirect(url_for('home')))
    response.set_cookie('medvision_session', '', expires=0)
    return response

if __name__ == "__main__":
    print("🚀 Starting MedVision Chatbot...")
    app.run(debug=True, host='0.0.0.0', port=5000)