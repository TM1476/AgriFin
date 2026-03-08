import os
import random
from flask import Flask, render_template, jsonify

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/register')
def index():
    return render_template('index.html')
    
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/onboarding')
def onboarding():
    return render_template('onboarding.html')

@app.route('/audit')
def audit():
    return render_template('audit.html')

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

@app.route('/api/score', methods=['POST'])
def get_score():
    import time
    time.sleep(1.5) 
    
    score = random.randint(720, 895)
    return jsonify({
        "score": score, 
        "status": "VERIFIED", 
        "details": "Land Records matched with Satellite NDVI (0.84)"
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
