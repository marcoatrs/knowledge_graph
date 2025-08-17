import re
from pathlib import Path

import fitz


def load_text_file(path: str) -> str:
    """Load a plain text file (.txt).

    Args:
        path (str): Path to the text file.
    Returns:
        str: File content.
    """
    file_path = Path(path)
    if not file_path.exists():
        return
    with open(path, "r") as f:
        file_content = f.read()
    return file_content


def load_pdf_file(path: str) -> str:
    """Extract text content from a PDF file.

    Args:
        path (str): Path to the PDF file.
    Returns:
        str: Extracted text.
    """
    file_path = Path(path)
    if not file_path.exists():
        return
    text = []
    with fitz.open(path) as doc:
        for page in doc:
            text.append(page.get_text("text"))
    full_text = "\n".join(text)
    full_text = re.sub(r"\n+", "\n", full_text)
    full_text = re.sub(r"[ \t]+", " ", full_text)
    full_text = "\n".join(line.strip() for line in full_text.splitlines()
                          if line.strip())
    return full_text


def chunk_text(text: str, chunk_size: int = 500) -> list[str]:
    """Split long text into chunks for embeddings.

    Args:
        text (str): Full text content.
        chunk_size (int): Approximate number of words per chunk.
    Returns:
        list[str]: List of text chunks.
    """
    chunks = []
    words = text.split()
    for i in range(0, len(words), chunk_size):
        chunk = words[i:i + chunk_size]
        chunks.append(" ".join(chunk))
    return chunks
