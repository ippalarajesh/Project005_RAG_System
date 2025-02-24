# ingestion/preprocessor.py
#Preprocess documents to clean them and prepare them for indexing.


def preprocess_document(doc):
    # Tokenization, cleaning, removing stop words, etc.
    return doc.lower().strip()