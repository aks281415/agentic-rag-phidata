from phi.embedder.openai import OpenAIEmbedder
# no functions of utils are being used currently

embedder = OpenAIEmbedder(model="text-embedding-3-small")

def generate_embedding(text: str):
    return embedder.get_embedding(text)

def batch_generate_embeddings(texts: list[str]):
    return embedder.get_embeddings(texts)
