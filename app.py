from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
import sqlite3

load_dotenv()

app = Flask(__name__)

DATABASE_URL = os.getenv('DATABASE_URL')

def get_db_connection():
    conn = sqlite3.connect(DATABASE_URL)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/analyze', methods=['POST'])
def analyze_hand():
    data = request.get_json()
    hand = data.get('hand')
    analysis = f"Received hand: {hand}. (This is where analysis would go.)"
    return jsonify({'analysis': analysis})

@app.route('/advice', methods=['POST'])
def get_advice():
    data = request.get_json()
    hand = data.get('hand')
    situation = data.get('situation')
    advice = f"Given the hand: {hand} and the situation: {situation}, (this is where advice would go.)"
    return jsonify({'advice': advice})

@app.route('/store', methods=['POST'])
def store_hand():
    data = request.get_json()
    hand = data.get('hand')
    analysis = data.get('analysis')
    advice = data.get('advice')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO poker_hands (hand, analysis, advice) VALUES (?, ?, ?)", (hand, analysis, advice))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Hand data stored successfully'})

if __name__ == '__main__':
    app.run(debug=True)