# rag_pipeline/__init__.py

#he rag_pipeline/__init__.py file, similar to the ingestion/__init__.py, is used to mark the rag_pipeline directory as a Python package. It imports relevant components from the rag_pipeline directory to facilitate easy access and modular integration. This would include the document retrieval logic, query processing, and response generation components.

#Here’s how you can structure the rag_pipeline/__init__.py file:

# Import core components for easy access in the RAG pipeline
from .document_retriever import DocumentRetriever
from .query_processor import process_query
from .response_generator import ResponseGenerator

# You may define versioning or other pipeline configuration here
__version__ = '1.0.0'

# Expose the essential classes and functions in the public API
__all__ = [
    'DocumentRetriever',
    'process_query',
    'ResponseGenerator'
]
#########################################################################################################################################################

# Example of using the RAG pipeline

from rag_pipeline import DocumentRetriever, process_query, ResponseGenerator

# Initialize components
db_client = ...  # Your ChromaDB or LlamaIndex client
retriever = DocumentRetriever(db_client)
response_generator = ResponseGenerator(openai_api_key='your-openai-api-key')

# Example query
query = "What is the capital of France?"

# Step 1: Preprocess the query
processed_query = process_query(query)

# Step 2: Retrieve relevant documents based on the query
retrieved_docs = retriever.retrieve_documents(processed_query)

# Step 3: Generate a response based on the query and retrieved documents
response = response_generator.generate_response(processed_query, retrieved_docs)

# Print the response
print(response)
