# utils/__init__.py

# Import core utility functions for easy access
from .text_preprocessor import preprocess_text, clean_text
from .logger import setup_logger, log_metrics
from .config_manager import load_config, save_config
from .file_handler import read_file, write_file
from .cache import setup_cache, get_from_cache, save_to_cache

# Define versioning or configuration related to the utils module
__version__ = '1.0.0'

# Expose the essential functions/classes in the public API
__all__ = [
    'preprocess_text',
    'clean_text',
    'setup_logger',
    'log_metrics',
    'load_config',
    'save_config',
    'read_file',
    'write_file',
    'setup_cache',
    'get_from_cache',
    'save_to_cache'
]
#################################################################################################################

# Example of using the utils module

from utils import preprocess_text, setup_logger, load_config, read_file, setup_cache

# 1. Preprocess text data
text = "This is an example sentence with extra spaces!   "
cleaned_text = preprocess_text(text)
print(cleaned_text)

# 2. Set up logger for system logs
logger = setup_logger()
logger.info("System started.")

# 3. Load configuration settings from a config file
config = load_config("config.json")
print(config)

# 4. Read data from a file (e.g., CSV, text document)
data = read_file("data.txt")
print(data)

# 5. Set up a caching mechanism to optimize system performance
setup_cache()
cached_data = get_from_cache("some_query")
if not cached_data:
    # Process the data and save it to cache
    save_to_cache("some_query", "processed_data")
