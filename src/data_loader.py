from pathlib import Path


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
    pass


def chunk_text(text: str, chunk_size: int = 500) -> list[str]:
    """Split long text into chunks for embeddings.

    Args:
        text (str): Full text content.
        chunk_size (int): Approximate number of words per chunk.
    Returns:
        list[str]: List of text chunks.
    """
    pass
