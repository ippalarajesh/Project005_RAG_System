
# Vectorize documents using embedding models and save them in ChromaDB.

import chromadb  # Example ChromaDB client

def vectorize_document(doc):
    # Example: Use an embedding model to convert the document into a vector
    vector = chromadb.embed_document(doc)
    return vector