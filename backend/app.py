from flask import Flask, jsonify
from flask_cors import CORS  # <-- Nouvelle importation

app = Flask(__name__)
CORS(app)  # <-- Ceci permettra à toutes les origines d'accéder à votre API

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({
        "data": "Hello from the backend!"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
