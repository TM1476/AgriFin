import os
import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index(): return render_template('index.html')

@app.route('/home')
def home(): return render_template('home.html')

@app.route('/onboarding')
def onboarding(): return render_template('onboarding.html')

@app.route('/audit')
def audit(): return render_template('audit.html')

@app.route('/analysis')
def analysis(): return render_template('analysis.html')

# API for Scorecard (Module 3a)
@app.route('/api/score', methods=['POST'])
def get_score():
    score = random.randint(720, 890)
    return jsonify({
        "score": score, 
        "status": "APPROVED", 
        "details": "Satellite Analysis: NDVI 0.82 (Healthy)"
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
