# server.py
from flask import Flask, jsonify
import time
import random
import os

app = Flask(__name__)

# Configuration via environment variables or defaults
TRANSLATION_DELAY = int(os.getenv("TRANSLATION_DELAY", 10))  # seconds
ERROR_RATE = float(os.getenv("ERROR_RATE", 0.1))  # 10% chance

start_time = time.time()

@app.route('/', methods=['GET'])
def home():
    return "HeyGen Video Translation Status API is running.", 200

@app.route('/status', methods=['GET'])
def status():
    elapsed = time.time() - start_time
    if elapsed < TRANSLATION_DELAY:
        return jsonify({"result": "pending"}), 200
    else:
        # After the delay, randomly return completed or error
        if random.random() < ERROR_RATE:
            return jsonify({"result": "error"}), 200
        return jsonify({"result": "completed"}), 200

@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return '', 204  

def run_server():
    
    app.run(port=5000, debug=False)

if __name__ == '__main__':
    run_server()