# utils/text_preprocessor.py

import re

def preprocess_text(text):
    """Preprocess the input text by cleaning and tokenizing."""
    text = clean_text(text)
    # Additional processing like tokenization, stemming, etc., can be added here
    return text

def clean_text(text):
    """Clean the input text by removing unnecessary characters."""
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with one
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text
