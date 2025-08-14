from duckduckgo_search import DDGS

def search_web(query, max_results=5):
    """Search the web using DuckDuckGo and return a list of results."""
    results_list = []
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=max_results)
        for r in results:
            results_list.append({
                "title": r.get("title"),
                "href": r.get("href"),
                "body": r.get("body")
            })
    return results_list

if __name__ == "__main__":
    # Test the function
    query = "latest AI news"
    search_results = search_web(query)
    for idx, res in enumerate(search_results, 1):
        print(f"{idx}. {res['title']}\n{res['href']}\n{res['body']}\n")
