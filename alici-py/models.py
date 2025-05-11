# models.py
from extensions import db  # Importa a instância db de extensions.py

class Knowledge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pergunta = db.Column(db.String(200), nullable=False)
    resposta = db.Column(db.String(200), nullable=False)
    vetor = db.Column(db.String(500), nullable=False)

    def __init__(self, pergunta, resposta, vetor):
        self.pergunta = pergunta
        self.resposta = resposta
        self.vetor = vetor

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mensagem = db.Column(db.String(500), nullable=False)
    resposta = db.Column(db.String(500), nullable=False)

    def __init__(self, mensagem, resposta):
        self.mensagem = mensagem
        self.resposta = resposta
