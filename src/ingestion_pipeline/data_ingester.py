# ingestion/data_ingester.py
import os
from .preprocessor import preprocess_document
from .vectorizer import vectorize_document

class DataIngester:
    def __init__(self, data_source: str, db_client):
        self.data_source = data_source
        self.db_client = db_client

    def ingest(self):
        documents = self.load_documents(self.data_source)
        for doc in documents:
            processed_doc = preprocess_document(doc)
            vector = vectorize_document(processed_doc)
            self.save_to_db(processed_doc, vector)

    def load_documents(self, source):
        # Load documents from CSV, web scraping, or databases
        if source.endswith('.csv'):
            return self.load_from_csv(source)
        # Add other data source loading methods as needed.
        return []

    def save_to_db(self, processed_doc, vector):
        # Save to ChromaDB (or LlamaIndex)
        self.db_client.add_document(processed_doc, vector)


