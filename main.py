import curses
from src.data_loader import load_text_file, load_pdf_file, chunk_text
from src.embeddings import generate_embeddings, semantic_search
from src.knowledge_graph import build_knowledge_graph, query_graph
from src.hybrid_engine import hybrid_query
from src.chatbot import chat_with_llm


def main(stdscr):
    curses.curs_set(1)  # Show cursor
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    # Chat history
    history = []
    input_buffer = ""

    # Dummy placeholders
    graph = None
    chunks = [
        "Cats are animals that like to play outside.",
        "Dogs are loyal companions.",
        "Birds can fly long distances."
    ]
    embeddings = generate_embeddings(chunks)

    while True:
        stdscr.clear()

        # Draw chat history
        for i, line in enumerate(history[-(height - 3):]):
            stdscr.addstr(i, 0, line[:width-1])

        # Draw input line
        stdscr.addstr(height - 2, 0, "> " + input_buffer)
        stdscr.refresh()

        key = stdscr.getch()

        # Handle input
        if key == curses.KEY_BACKSPACE or key == 127:
            input_buffer = input_buffer[:-1]
        elif key in (curses.KEY_ENTER, 10, 13):
            query = input_buffer.strip()
            if query.lower() in ["exit", "quit"]:
                break

            if query:
                # --- semantic search simple ---
                results = semantic_search(query, embeddings, chunks, top_k=1)
                answer = results[0] if results else "[no match]"

                history.append("You: " + query)
                history.append("Bot: " + answer)
                # # --- Hybrid Query + Chatbot response ---
                # results = hybrid_query(query, graph, embeddings, chunks)
                # answer = chat_with_llm(query, results)

            input_buffer = ""
        elif 32 <= key <= 126:  # Printable characters
            input_buffer += chr(key)


if __name__ == "__main__":
    curses.wrapper(main)
