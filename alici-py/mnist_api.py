from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)
model = load_model('mnist_model.h5')

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
    app.run(debug=True, port=5001)
