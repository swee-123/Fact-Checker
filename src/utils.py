import hashlib
import json

def cache_result(key: str, result: str, cache_file="cache.json"):
    """
    Save result to a local JSON cache to reduce repeated API calls.
    """
    try:
        try:
            with open(cache_file, "r") as f:
                cache = json.load(f)
        except FileNotFoundError:
            cache = {}

        cache[key] = result
        with open(cache_file, "w") as f:
            json.dump(cache, f, indent=4)
    except Exception as e:
        print(f"Error caching result: {e}")

def get_cache(key: str, cache_file="cache.json") -> str:
    """
    Retrieve a cached result if available.
    """
    try:
        with open(cache_file, "r") as f:
            cache = json.load(f)
        return cache.get(key, None)
    except Exception:
        return None

def hash_text(text: str) -> str:
    """Generate a simple hash for caching purposes."""
    return hashlib.sha256(text.encode()).hexdigest()


# --- New formatting function for True/False output ---
def format_result_true_false(claim, is_correct, correct_statement=None):
    """
    Format the fact-check result:
    - ✅ True if claim is correct
    - ❌ False + correct statement if claim is wrong
    """
    if is_correct:
        return f"**Claim:** {claim}\n✅ True"
    else:
        return f"**Claim:** {claim}\n❌ False\n**Correct Statement:** {correct_statement}"
