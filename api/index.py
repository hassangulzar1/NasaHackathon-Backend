from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from utils.qdrant_helper import get_context
from utils.groq_helper import generate_response

app = Flask(__name__)
CORS(app)

@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    try:
        data = request.get_json()
        if not data or 'query' not in data:
            return jsonify({'error': 'No query provided'}), 400
        
        user_query = data['query']
        
        # Get context from Qdrant
        context_response = get_context(user_query)
        
        # Generate response using Groq
        chat_response = generate_response(user_query, context_response)
        
        return jsonify({'response': chat_response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({'status': 'healthy'}), 200