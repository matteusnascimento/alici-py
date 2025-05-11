import openai
from dotenv import load_dotenv

load_dotenv()

# Chave da API OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

def gerar_resposta(pergunta):
    """Gera a resposta usando o GPT-4 ou busca por respostas similares no banco de dados."""
    resposta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é a Alici, uma assistente simpática e inteligente."},
            {"role": "user", "content": pergunta}
        ]
    )

    texto = resposta['choices'][0]['message']['content']
    return texto
