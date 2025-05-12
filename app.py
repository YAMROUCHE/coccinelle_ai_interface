
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index_route():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json.get('question', '')
    if not question:
        return jsonify({'answer': 'Veuillez poser une question.'})
    # Réponse simulée — à remplacer par GPT ou Pinecone
    answer = f"Réponse simulée pour : '{question}'"
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
