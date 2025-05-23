import re

def detectar_intencao(pergunta):
    pergunta = pergunta.lower()

    if re.search(r"\b(mostre|exiba|imagem|foto|veja)\b", pergunta):
        return "imagem"

    elif re.search(r"\b(resuma|resumo|resumir|encurte)\b", pergunta):
        return "resumo"

    elif re.search(r"\b(traduza|traduzir|tradução|em inglês|para o inglês|para português)\b", pergunta):
        return "traduzir"

    elif re.search(r"\b(defina|o que é|significa|significado)\b", pergunta):
        return "definicao"

    elif re.search(r"\b(converta|converter|transformar|em metros|em graus|em reais)\b", pergunta):
        return "conversao"

    return "geral"
