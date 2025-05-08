import os
from openai import OpenAI
from models import treinar_modelo, buscar_resposta_similar
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()  # <- NÃO passar api_key aqui

def gerar_resposta(pergunta):
    similar = buscar_resposta_similar(pergunta)
    if similar:
        return similar

    resposta = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é a Alici, uma assistente simpática e inteligente."},
            {"role": "user", "content": pergunta},
        ]
    )
    texto = resposta.choices[0].message.content
    treinar_modelo(pergunta, texto)
    return texto
