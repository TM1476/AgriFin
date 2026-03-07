import os
import random
from flask import Flask, render_template, jsonify

app = Flask(__name__, static_folder='static', template_folder='templates')

# 1. Landing Page (The new Hero section you just shared)
@app.route('/')
def home():
    return render_template('home.html')

# 2. Registration/Login (The Firebase page)
@app.route('/register')
def index():
    return render_template('index.html')

# 3. Voice Intake (Module 4a)
@app.route('/onboarding')
def onboarding():
    return render_template('onboarding.html')

# 4. Document Scan (Module 3b)
@app.route('/audit')
def audit():
    return render_template('audit.html')

# 5. AI Result (Module 3a)
@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

# API for Module 3a: Scoring Logic
@app.route('/api/score', methods=['POST'])
def get_score():
    score = random.randint(720, 895)
    return jsonify({
        "score": score, 
        "status": "SUCCESS", 
        "details": "Satellite NDVI Analysis: 0.84 (Optimal)"
    })

if __name__ == '__main__':
    # Use environment port for Render, fallback to 5000 for local
    port = int(os.environ.get("PORT", 5000))
    # host='0.0.0.0' is required for cloud deployment
    app.run(host='0.0.0.0', port=port, debug=True)
