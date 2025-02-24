# rag_pipeline/document_retriever.py
class DocumentRetriever:
    def __init__(self, db_client):
        self.db_client = db_client

    def retrieve_documents(self, query):
        # Retrieve documents from ChromaDB or LlamaIndex
        return self.db_client.retrieve(query)

