# database.py
from flask_sqlalchemy import SQLAlchemy
from models import Knowledge, Message  # Importa ambos os modelos de uma vez

db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados

def carregar_conhecimentos():
    conhecimentos = Knowledge.query.all()
    conhecimentos_list = []
    for conhecimento in conhecimentos:
        conhecimentos_list.append({
            'id': conhecimento.id,
            'question': conhecimento.question,
            'answer': conhecimento.answer,
            'embedding': conhecimento.embedding
        })
    return conhecimentos_list
