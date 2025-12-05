import os

# The knowledge base file is assumed to be in the parent directory
KB_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'knowledge_base', 'neuropsychologist_kb.md')

def load_knowledge_base() -> str:
    """
    Loads the entire content of the knowledge base file.
    In a simple RAG implementation, the entire KB is passed to the LLM.
    For a more complex implementation, this function would include:
    1. Text chunking
    2. Embedding generation
    3. Vector database search (not implemented here for simplicity)
    4. Context assembly

    Returns:
        The full content of the knowledge base as a string.
    """
    try:
        with open(KB_FILE_PATH, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Knowledge base file not found at {KB_FILE_PATH}")
        return "База знаний недоступна. Проект: Нейропсихолог. Суть: Научные методики для решения психологических проблем. Цена: 250 рублей."

# Load the knowledge base once at startup
KNOWLEDGE_BASE_CONTENT = load_knowledge_base()

def get_context_for_query(query: str) -> str:
    """
    Retrieves the relevant context from the knowledge base for a given query.
    In this simple implementation, we return the entire knowledge base,
    relying on the LLM's ability to use the relevant parts.

    Args:
        query: The user's message.

    Returns:
        The context string to be passed to the LLM.
    """
    # In a real RAG system, a search would happen here.
    # For this task, we pass the entire pre-loaded KB content.
    return KNOWLEDGE_BASE_CONTENT

# Example usage (for testing purposes, not run in production)
if __name__ == '__main__':
    kb = load_knowledge_base()
    print("--- Knowledge Base Loaded ---")
    print(kb[:500] + "...")
    print("-----------------------------")
