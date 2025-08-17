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
