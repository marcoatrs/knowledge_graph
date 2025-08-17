from sentence_transformers import SentenceTransformer

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
                    top_k: int = 5) -> list[str]:
    """Perform semantic search comparing the query against embeddings.

    Args:
        query (str): User question or search string.
        embeddings (list[list[float]]): Vectors for text chunks.
        chunks (list[str]): Original text chunks.
        top_k (int): Number of top results to return.
    Returns:
        list[str]: List of the most relevant chunks.
    """
    pass
