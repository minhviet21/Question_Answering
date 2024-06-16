from sentence_transformers import SentenceTransformer

model_embedding = SentenceTransformer('bkai-foundation-models/vietnamese-bi-encoder')

def embed_question(question):
    return model_embedding.encode(question)