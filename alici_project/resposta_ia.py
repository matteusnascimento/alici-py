from ai_engine import gerar_resposta_openai
from modela import gerar_embedding, encontrar_resposta_similar
from database import salvar_conversa, obter_todas_conversas

def obter_resposta(pergunta):
    conversas = obter_todas_conversas()
    embedding_pergunta = gerar_embedding(pergunta)
    resposta_similar = encontrar_resposta_similar(embedding_pergunta, conversas)
    if resposta_similar:
        return resposta_similar
    resposta_nova = gerar_resposta_openai(pergunta)
    salvar_conversa(pergunta, resposta_nova, embedding_pergunta)
    return resposta_nova
