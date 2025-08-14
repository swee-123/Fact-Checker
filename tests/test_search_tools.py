import pytest
from src.search_tools import web_search

def test_web_search_returns_results():
    query = "current president of the United States"
    results = web_search(query, max_results=2)
    assert isinstance(results, list)
    assert len(results) > 0
    assert all("title" in r and "snippet" in r for r in results)
