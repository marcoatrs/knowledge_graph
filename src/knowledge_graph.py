def extract_entities_relations(text: str) -> list[tuple[str, str, str]]:
    """Extract entities and relations from text using NLP.

    Args:
        text (str): Input text.
    Returns:
        list[tuple[str, str, str]]: List of triplets (entity1, relation, entity2).
    """
    pass


def build_knowledge_graph(triplets: list[tuple[str, str, str]]):
    """Build a knowledge graph from entity-relation triplets.

    Args:
        triplets (list[tuple[str, str, str]]): Extracted triplets.
    Returns:
        object: Graph object (e.g., networkx.Graph or Neo4j connection).
    """
    pass


def query_graph(graph, query: str) -> list[str]:
    """Query the knowledge graph to answer questions.

    Args:
        graph (object): The knowledge graph.
        query (str): User question in natural language or keyword.
    Returns:
        list[str]: Answers found in the graph.
    """
    pass
