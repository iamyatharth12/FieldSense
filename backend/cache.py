import hashlib

# Simple in-memory dictionary cache
_cache = {}

def get_image_hash(image_bytes: bytes) -> str:
    """Returns the MD5 hash of the given image bytes."""
    return hashlib.md5(image_bytes).hexdigest()

def get_cached_result(image_hash: str):
    """Returns the cached result if it exists, otherwise None."""
    return _cache.get(image_hash)

def set_cached_result(image_hash: str, result: dict):
    """Stores the result in the cache."""
    _cache[image_hash] = result
