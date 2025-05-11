# app.py
import numpy as np
from flask_sqlalchemy import SQLAlchemy
from tensorflow.keras.models import load_model

import os
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from tensorflow.keras.models import load_model
from extensions import db  # Importa o db de extensions.py
from ai_engine import responder_alici
from database import init_app, Message  # Importa a inicialização do banco e a model Message

# Inicialização do Flask
app = Flask(__name__)

# Carregar variáveis de ambiente
load_dotenv()

# Configuração do banco de dados com a URL do Neon
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://neondb_owner:npg_YA5DVX0fvWrg@ep-frosty-shape-a8fhb2m2-pooler.eastus2.azure.neon.tech/neondb?sslmode=require')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco de dados com o app
init_app(app)


# Criação da instância do SQLAlchemy
db = SQLAlchemy()

# Inicialização do SQLAlchemy com a app
db.init_app(app)

# Resto da configuração do seu aplicativo


# Carregar o modelo MNIST
model = load_model('mnist_model.h5')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mensagens', methods=['GET'])
def mensagens():
    messages = Message.query.all()
    return render_template('admin.html', messages=messages)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    alici_response = responder_alici(user_message)

    # Armazenando a conversa
    message_user = Message(mensagem=user_message, resposta=alici_response)
    db.session.add(message_user)
    db.session.commit()

    return jsonify({'response': alici_response})

@app.route('/predict-digit', methods=['POST'])
def predict_digit():
    data = request.get_json()
    if 'pixels' not in data:
        return jsonify({'error': 'Parâmetro "pixels" não encontrado'}), 400
    try:
        img = np.array(data['pixels']).reshape(1, 28, 28)
        img = img / 255.0
        prediction = model.predict(img)
        digit = int(np.argmax(prediction))
        confidence = float(np.max(prediction))
        return jsonify({'digit': digit, 'confidence': confidence})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
