# utils/config_manager.py

import json

def load_config(filename):
    """Load configuration data from a JSON file."""
    with open(filename, "r") as file:
        return json.load(file)

def save_config(config, filename):
    """Save configuration data to a JSON file."""
    with open(filename, "w") as file:
        json.dump(config, file, indent=4)


######################################################################################################################################################################
# utils/config_manager.py
from dotenv import load_dotenv
import os

def load_config():
    """
    Load configuration from environment variables and fallback to config.json if necessary.
    """
    load_dotenv()  # Load environment variables from a .env file

    config = {
        "llama_index": {
            "index_path": os.getenv("LLAMA_INDEX_PATH", "default/path/to/llama_index")
        },
        "chroma_db": {
            "db_path": os.getenv("CHROMA_DB_PATH", "default/path/to/chroma_db")
        },
        "chatgpt_model": {
            "api_key": os.getenv("OPENAI_API_KEY"),
            "model": "gpt-4",  # Default model
            "temperature": float(os.getenv("GPT_TEMPERATURE", 0.7))
        },
        "logging": {
            "log_level": os.getenv("LOG_LEVEL", "INFO"),
            "log_file": os.getenv("LOG_FILE", "logs/system.log")
        }
    }
    
    return config
