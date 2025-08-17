import os

import pytest

from src.data_loader import chunk_text, load_text_file

SAMPLE_TEXT = "Python is a programming language created by Guido van Rossum in 1991."


def test_load_text_file(tmp_path):
    """
    Test that load_text_file correctly reads a text file.
    """
    # Create a temporary text file
    file_path = tmp_path / "sample.txt"
    file_path.write_text(SAMPLE_TEXT)

    # Call function
    content = load_text_file(str(file_path))

    assert isinstance(content, str)
    assert "Python" in content
    assert "1991" in content


def test_chunk_text():
    """
    Test that chunk_text splits text correctly.
    """
    text = " ".join([f"word{i}" for i in range(100)])  # 100 words
    chunks = chunk_text(text, chunk_size=20)

    assert isinstance(chunks, list)
    assert all(isinstance(c, str) for c in chunks)
    assert len(chunks) >= 5  # since 100 / 20 = 5
