import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# ==== API KEYS ====
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Set in your .env file

# ==== MODEL SETTINGS ====
MODEL_PARAMS = {
    "temperature": 0.2,   # Lower = more factual responses
    "max_tokens": 500
}

# ==== SEARCH SETTINGS ====
SEARCH_ENGINE = "duckduckgo"  # Can be extended later for SerpAPI, Bing, etc.
MAX_SEARCH_RESULTS = 3

# ==== CACHE SETTINGS ====
CACHE_FILE = "cache.json"
