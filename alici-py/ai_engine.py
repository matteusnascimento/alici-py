# ai_engine.py
import numpy as np
from embedding_tf import gerar_embedding
from database import carregar_conhecimentos

def similaridade(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)
    if np.linalg.norm(v1) == 0 or np.linalg.norm(v2) == 0:
        return 0.0
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def responder_alici(pergunta_usuario):
    emb_usuario = gerar_embedding(pergunta_usuario)
    conhecimentos = carregar_conhecimentos()

    melhor_sim = 0
    melhor_resp = "Desculpe, ainda não aprendi isso."

    for conhecimento in conhecimentos:
        vetor_embedding = np.array(conhecimento['embedding'])
        sim = similaridade(emb_usuario, vetor_embedding)
        if sim > melhor_sim:
            melhor_sim = sim
            melhor_resp = conhecimento['answer']

    return melhor_resp
