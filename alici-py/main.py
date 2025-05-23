# main.py

from flask import Flask, render_template, request, jsonify
from resposta import responder  # Função que responde perguntas de texto
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import os

# Define os caminhos corretos para templates e arquivos estáticos
template_dir = os.path.join(os.path.dirname(__file__), 'Web', 'templates')
static_dir = os.path.join(os.path.dirname(__file__), 'Web', 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# Carregar o modelo de classificação de animais (CIFAR-100)
modelo = load_model("modelo_animais_cifar100.h5")

# Classes do CIFAR-100 para mapear índices para nomes
classes = [
    'apple', 'aquarium_fish', 'baby', 'bear', 'beaver', 'bed', 'bee', 'beetle', 'bicycle', 'bottle',
    'bowl', 'boy', 'bridge', 'bus', 'butterfly', 'cabbage', 'camel', 'can', 'castle', 'caterpillar',
    'cattle', 'chair', 'chimpanzee', 'clock', 'cloud', 'cockroach', 'couch', 'crab', 'crocodile',
    'cup', 'dinosaur', 'dolphin', 'elephant', 'flatfish', 'forest', 'fox', 'girl', 'hamster',
    'house', 'kangaroo', 'keyboard', 'lamp', 'lawn_mower', 'leopard', 'lion', 'lizard', 'lobster',
    'man', 'maple_tree', 'motorcycle', 'mountain', 'mouse', 'mushroom', 'oak_tree', 'orange',
    'orchid', 'otter', 'palm_tree', 'pear', 'pickup_truck', 'pine_tree', 'plain', 'plate', 'poppy',
    'porcupine', 'possum', 'rabbit', 'raccoon', 'ray', 'road', 'rocket', 'rose', 'sea', 'seal',
    'shark', 'shrew', 'skunk', 'skyscraper', 'snail', 'snake', 'spider', 'squirrel', 'streetcar',
    'sunflower', 'sweet_pepper', 'table', 'tank', 'telephone', 'television', 'tiger', 'tractor',
    'train', 'trout', 'tulip', 'turtle', 'wardrobe', 'whale', 'willow_tree', 'wolf', 'woman',
    'worm'
]

def preprocessar_imagem(file_path):
    img = Image.open(file_path).resize((32, 32))
    img = np.array(img) / 255.0
    return img.reshape(1, 32, 32, 3)

def classificar_imagem(file_path):
    img = preprocessar_imagem(file_path)
    predicoes = modelo.predict(img)
    indice_classe = np.argmax(predicoes)
    nome_classe = classes[indice_classe]
    confianca = float(predicoes[0][indice_classe])
    return nome_classe, confianca

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/perguntar", methods=["POST"])
def perguntar():
    dados = request.get_json()
    pergunta = dados.get("pergunta", "")
    resposta = responder(pergunta)
    return jsonify({"resposta": resposta})

@app.route("/classificar", methods=["POST"])
def classificar():
    if "imagem" not in request.files:
        return jsonify({"erro": "Nenhuma imagem enviada"}), 400

    imagem = request.files["imagem"]
    caminho_temporario = os.path.join("uploads", imagem.filename)
    os.makedirs("uploads", exist_ok=True)
    imagem.save(caminho_temporario)

    try:
        classe, confianca = classificar_imagem(caminho_temporario)
    except Exception as e:
        return jsonify({"erro": f"Erro ao processar a imagem: {str(e)}"}), 500
    finally:
        os.remove(caminho_temporario)

    return jsonify({"classe": classe, "confianca": confianca})

if __name__ == "__main__":
    app.run(debug=True)
