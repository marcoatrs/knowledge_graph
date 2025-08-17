import networkx as nx

from src import knowledge_graph as kg


def test_extract_entities_relations():
    text = "Alice knows Bob. Bob works at ACME"
    triplets = kg.extract_entities_relations(text)
    expected = [("Alice", "know", "Bob"), ("Bob", "work", "ACME")]
    assert all(t in triplets for t in expected)


def test_build_knowledge_graph():
    triplets = [("Alice", "knows", "Bob"), ("Bob", "work", "ACME")]
    graph = kg.build_knowledge_graph(triplets)
    assert isinstance(graph, nx.DiGraph) or isinstance(graph, nx.Graph)
    assert ("Alice", "Bob") in graph.edges
    assert ("Bob", "ACME") in graph.edges


def test_query_graph():
    triplets = [
        ("Alice", "knows", "Bob"),
        ("Bob", "work", "ACME"),
    ]
    graph = kg.build_knowledge_graph(triplets)
    results = kg.query_graph(graph, "Alice")
    assert any("Bob" in r for r in results)
    results = kg.query_graph(graph, "Bob")
    assert any("ACME" in r for r in results)
