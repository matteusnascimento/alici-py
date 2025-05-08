from flask import Flask, render_template, request, jsonify
import numpy as np
from PIL import Image, ImageOps
import tensorflow as tf
from database import init_app, db
from models import Message

app = Flask(__name__)
init_app(app)

# Criação das tabelas no banco de dados (se não existirem)
with app.app_context():
	db.create_all()

# Carrega o modelo MNIST
model = tf.keras.models.load_model('mnist_model.h5')


@app.route('/')
def home():
	return render_template('index.html')


@app.route('/predict_text', methods=['POST'])
def predict_text():
	data = request.get_json()
	user_input = data.get('text', '')
	
	# Resposta simulada
	response = f"Você disse: '{user_input}'"
	
	# Armazena no banco de dados
	db.session.add(Message(sender='user', content=user_input))
	db.session.add(Message(sender='ai', content=response))
	db.session.commit()
	
	return jsonify({'response': response})


@app.route('/predict_image', methods=['POST'])
def predict_image():
	if 'image' not in request.files:
		return jsonify({'response': 'Nenhuma imagem enviada.'})
	
	image = request.files['image']
	img = Image.open(image).convert('L').resize((28, 28))
	img = ImageOps.invert(img)
	img = np.array(img) / 255.0
	img = img.reshape(1, 28, 28)
	
	prediction = model.predict(img)
	predicted_digit = int(np.argmax(prediction))
	
	response = f'Dígito reconhecido: {predicted_digit}'
	
	# Armazena no banco de dados
	db.session.add(Message(sender='user', content='[imagem]'))
	db.session.add(Message(sender='ai', content=response))
	db.session.commit()
	
	return jsonify({'response': response})


@app.route('/predict_audio', methods=['POST'])
def predict_audio():
	response = 'Reconhecimento de áudio ainda não implementado.'
	# Armazena no banco de dados
	db.session.add(Message(sender='user', content='[áudio]'))
	db.session.add(Message(sender='ai', content=response))
	db.session.commit()
	return jsonify({'response': response})


# Rota para visualizar as mensagens armazenadas no banco de dados
@app.route('/admin/messages')
def view_messages():
	messages = Message.query.order_by(Message.timestamp.desc()).all()  # Busca as mensagens mais recentes
	return render_template('admin_messages.html', messages=messages)


if __name__ == '__main__':
	app.run(debug=True)
