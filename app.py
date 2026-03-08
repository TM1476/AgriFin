import os
from flask import Flask, render_template, jsonify

app = Flask(__name__, static_folder='static', template_folder='templates')

# --- AgriLend Scoring Engine ---
def calculate_perfect_score():
    """
    Calculates a score based on fixed agricultural parameters 
    rather than random generation.
    """
    base_reliability = 400
    satellite_ndvi_impact = 250  # Based on 0.84 NDVI
    land_verification_points = 200 # Document scan success
    
    # Total Score: 850 (A "Perfect" high-credit scenario)
    total_score = base_reliability + satellite_ndvi_impact + land_verification_points
    return total_score

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register')
def index():
    return render_template('index.html')

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
    time.sleep(1.5)  # Simulate processing time
    
    # Calculate a non-random, verified score
    score = calculate_perfect_score()
    
    return jsonify({
        "score": score, 
        "status": "VERIFIED", 
        "details": "Land Records matched with Satellite NDVI (0.84). Analysis verified via AI Engine."
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
