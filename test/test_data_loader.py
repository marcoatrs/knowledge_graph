from pathlib import Path
from tempfile import NamedTemporaryFile

import fitz

from src.data_loader import chunk_text, load_pdf_file, load_text_file

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


def test_load_pdf_file():

    def create_test_pdf(text: str, path: str):
        doc = fitz.open()
        page = doc.new_page()
        page.insert_text((72, 72), text)
        doc.save(path)
        doc.close()

    test_text = "Hello, this is a test PDF."

    with NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
        create_test_pdf(test_text, tmp.name)
        tmp_path = tmp.name

    extracted_text = load_pdf_file(tmp_path)

    assert test_text in extracted_text

    Path(tmp_path).unlink()
