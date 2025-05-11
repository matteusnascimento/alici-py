import tensorflow_hub as hub
import os
import json

# Carregando o modelo do TensorFlow Hub apenas uma vez
embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

def gerar_embedding(texto):
    """
    Gera o embedding para o texto fornecido usando o modelo universal-sentence-encoder.
    """
    vetor = embed([texto])[0].numpy()  # Obtém o vetor de embedding
    return vetor.tolist()  # Retorna como lista para ser compatível com o banco de dados

def carregar_base_conhecimento():
    """
    Carrega a base de conhecimento de um arquivo JSON.
    """
    arquivo_path = "caminho/do/arquivo/base_conhecimento.json"
    if os.path.exists(arquivo_path):
        with open(arquivo_path, 'r') as file:
            return json.load(file)
    else:
        return []  # Retorna uma lista vazia se o arquivo não for encontrado

def salvar_em_arquivo(base):
    """
    Salva a base de conhecimento em um arquivo JSON.
    """
    arquivo_path = "caminho/do/arquivo/base_conhecimento.json"
    with open(arquivo_path, 'w') as file:
        json.dump(base, file)

# Outras funções podem ser adicionadas para gerenciar o conteúdo da base de conhecimento
