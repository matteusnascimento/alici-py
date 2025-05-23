# engine.py

def responder_com_modelo(pergunta):
    pergunta = pergunta.strip().lower()
    if "seu nome" in pergunta:
        return "Meu nome é Alici, sua assistente de IA."
    elif "oi" in pergunta or "olá" in pergunta:
        return "Olá! Como posso te ajudar hoje?"
    else:
        return "Desculpe, ainda estou aprendendo sobre isso."
