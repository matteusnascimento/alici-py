from intencao import detectar_intencao
from database import buscar_resposta, salvar_conversa
from engine import responder_com_modelo
from web_search import buscar_na_web

RESPOSTAS_FRACAS = [
    "não sei",
    "ainda estou aprendendo",
    "desculpe",
    "não posso responder",
    "não encontrei nada",
    "não tenho certeza",
    "não consigo",
    "não está disponível"
]

def resposta_invalida(resposta):
    if not resposta:
        return True
    texto = resposta.strip().lower()
    return any(frase in texto for frase in RESPOSTAS_FRACAS) or len(texto) < 5

def responder(pergunta):
    pergunta_processada = pergunta.strip().lower()
    print("Pergunta processada:", pergunta_processada)

    # Etapa 0: Detectar intenção
    intencao = detectar_intencao(pergunta_processada)
    print("Intenção detectada:", intencao)

    # 1. Buscar no banco de dados
    resposta = buscar_resposta(pergunta_processada)
    if resposta and not resposta_invalida(resposta):
        print("Resposta encontrada no banco.")
        return resposta

    # 2. Se a intenção for especial, usar diretamente a web
    if intencao in ["imagem", "resumo", "traduzir", "definicao", "conversao"]:
        print("Usando busca na web com base na intenção detectada.")
        resposta = buscar_na_web(pergunta)

    else:
        # 3. Tentar responder com modelo local
        resposta = responder_com_modelo(pergunta)
        if resposta_invalida(resposta):
            print("Modelo falhou ou resposta fraca. Buscando na web...")
            resposta = buscar_na_web(pergunta)

    # 4. Salvar a conversa
    salvar_conversa(pergunta_processada, resposta)
    return resposta
