import math

from src.embeddings import generate_embeddings, semantic_search


def test_generate_embeddings():
    chunks = ["Hello world", "This text is a test", "Another chunk of test"]

    embeddings = generate_embeddings(chunks)

    assert len(embeddings) == len(chunks)

    for vec in embeddings:
        assert isinstance(vec, list)
        assert all(isinstance(x, float) for x in vec)
        assert all(not math.isnan(x) for x in vec)


def test_semantic_search():
    # Chunks
    chunks = [
        "The cat sleeps on the windowsill", "I like eating chocolate",
        "Dogs are running in the park", "Today is very sunny",
        "Learning to program in Python"
    ]

    # Mock embeddings
    embeddings = [
        [0.9, 0.1, 0.0],  # cat-related
        [0.0, 0.9, 0.0],  # chocolate
        [0.8, 0.2, 0.1],  # dogs
        [0.0, 0.0, 0.9],  # sun
        [0.1, 0.0, 0.9],  # python
    ]

    results = semantic_search(query="Animals playing outside",
                              embeddings=embeddings,
                              chunks=chunks,
                              top_k=2,
                              query_embedding=[0.85, 0.15, 0.0])

    assert len(results) <= 2
    assert all(res in chunks for res in results)
    assert "cat" in results[0] or "Dogs" in results[0]
