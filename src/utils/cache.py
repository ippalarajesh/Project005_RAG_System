# utils/cache.py

# Simple in-memory cache using a dictionary
cache = {}

def setup_cache():
    """Initialize the cache (if needed)."""
    global cache
    cache = {}  # Reset cache (can be extended to use an external caching service)

def get_from_cache(key):
    """Retrieve data from the cache by key."""
    return cache.get(key, None)

def save_to_cache(key, value):
    """Save data to the cache."""
    cache[key] = value
