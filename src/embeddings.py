from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings(chunks: list[str]) -> list[list[float]]:
    """Generate vector embeddings for each text chunk.

    Args:
        chunks (list[str]): List of text chunks.
    Returns:
        list[list[float]]: List of embedding vectors.
    """
    embeddings = model.encode(chunks, show_progress_bar=False)
    return embeddings.tolist()


def semantic_search(query: str,
                    embeddings: list[list[float]],
                    chunks: list[str],
                    top_k: int = 5,
                    query_embedding: list[float] = None) -> list[str]:
    """Perform semantic search comparing the query against embeddings.

    Args:
        query (str): User question or search string.
        embeddings (list[list[float]]): Vectors for text chunks.
        chunks (list[str]): Original text chunks.
        top_k (int): Number of top results to return.
        query_embedding (list[float]) If provided, it will be used instead of generating a new one.
    Returns:
        list[str]: List of the most relevant chunks.
    """
    if query_embedding is not None:
        query_vector = [query_embedding]
    else:
        query_vector = model.encode([query])
    similarities = cosine_similarity(query_vector, embeddings).flatten()
    top_index = similarities.argsort()[-top_k:][::-1]
    return [chunks[i] for i in top_index]
