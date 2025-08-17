def hybrid_query(query: str, graph, embeddings: list[list[float]], chunks: list[str]) -> list[str]:
    """Hybrid search engine: first try to answer with the graph,
    fallback to semantic search if no clear results are found.

    Args:
        query (str): User question.
        graph (object): Knowledge graph.
        embeddings (list[list[float]]): Embedding vectors.
        chunks (list[str]): Original text chunks.
    Returns:
        list[str]: Relevant fragments or answers.
    """
    pass
