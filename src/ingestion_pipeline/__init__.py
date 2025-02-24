# ingestion/__init__.py

#The ingestion/__init__.py file is typically used to mark the ingestion directory as a Python package and to import relevant modules that users of the package might need. 
# It's also a good place to handle package-level configuration or setup. Since the ingestion directory contains files like data_ingester.py, preprocessor.py, and vectorizer.py, 
# the __init__.py file can be structured to make these modules available for easy import.


# Import the core components for easy access
from .data_ingester import DataIngester
from .preprocessor import preprocess_document
from .vectorizer import vectorize_document

# You may also define versioning or other configuration information here
__version__ = '1.0.0'

# If needed, expose specific functions or classes as part of the public API
__all__ = [
    'DataIngester', 
    'preprocess_document', 
    'vectorize_document'
]



################################################################################################

# Example of how to use the ingestion module
from ingestion import DataIngester, preprocess_document, vectorize_document

# Initialize the data ingester
data_ingester = DataIngester(data_source="documents.csv", db_client=db_client)

# Ingest the data
data_ingester.ingest()

# Example of preprocessing and vectorizing a document
document = "This is a sample document."
processed_doc = preprocess_document(document)
vector = vectorize_document(processed_doc)
