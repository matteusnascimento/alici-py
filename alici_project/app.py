from flask import Flask, request, render_template
from resposta_ia import obter_resposta
from database import criar_tabela

app = Flask(__name__)
criar_tabela()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/perguntar', methods=['POST'])
def perguntar():
    pergunta = request.form['pergunta']
    resposta = obter_resposta(pergunta)
    return {'resposta': resposta}

if __name__ == '__main__':
    app.run(debug=True)
