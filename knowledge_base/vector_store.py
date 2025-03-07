from phi.vectordb.pgvector import PgVector
from phi.embedder.openai import OpenAIEmbedder
from phi.vectordb.pgvector import PgVector, SearchType
def create_vector_store(collection: str, db_url: str):
    return PgVector(
        table_name=collection,
        db_url=db_url,
        embedder=OpenAIEmbedder(model="text-embedding-3-small",
                                search_type=SearchType.hybrid)
    )
