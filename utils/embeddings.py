from phi.embedder.openai import OpenAIEmbedder

embedder = OpenAIEmbedder(model="text-embedding-3-small")

def generate_embedding(text: str):
    return embedder.get_embedding(text)

def batch_generate_embeddings(texts: list[str]):
    return embedder.get_embeddings(texts)
