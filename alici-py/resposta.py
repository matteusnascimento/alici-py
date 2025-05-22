# resposta.py

from database import buscar_resposta, salvar_conversa
from engine import responder_com_modelo
from web_search import buscar_na_web

def responder(pergunta):
    pergunta_processada = pergunta.strip().lower()
    print("Pergunta processada:", pergunta_processada)

    # 1. Tenta buscar no banco
    resposta = buscar_resposta(pergunta_processada)
    if resposta:
        print("Resposta encontrada no banco.")
        return resposta

    # 2. Usa o modelo
    resposta = responder_com_modelo(pergunta)
    if not resposta or "não sei" in resposta.lower():
        # 3. Busca na web
        print("Buscando na web...")
        resposta = buscar_na_web(pergunta)

    # 4. Salva a resposta
    salvar_conversa(pergunta_processada, resposta)
    return resposta
