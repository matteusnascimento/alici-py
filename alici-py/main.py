# main.py

from flask import Flask, render_template, request, jsonify
from resposta import responder  # <- Correto agora
import os

# Define os caminhos corretos para templates e arquivos estáticos
template_dir = os.path.join(os.path.dirname(__file__), 'Web', 'templates')
static_dir = os.path.join(os.path.dirname(__file__), 'Web', 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/perguntar", methods=["POST"])
def perguntar():
    dados = request.get_json()
    pergunta = dados.get("pergunta", "")
    resposta = responder(pergunta)  # <- Chamando a função correta
    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run(debug=True)
