
from langchain_ollama import OllamaEmbeddings

def get_embedding_function():
    # Use OllamaEmbeddings to populate the embeddings variable
    embeddings = OllamaEmbeddings(model="llama3.3")
    return embeddings