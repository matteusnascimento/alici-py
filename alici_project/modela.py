from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('all-MiniLM-L6-v2')

def gerar_embedding(texto):
    return model.encode(texto).tolist()

def encontrar_resposta_similar(embedding_pergunta, conversas):
    for pergunta, resposta, emb_string in conversas:
        emb = list(map(float, emb_string.split(',')))
        sim = util.cos_sim(embedding_pergunta, [emb])[0][0].item()
        if sim > 0.85:
            return resposta
    return None
