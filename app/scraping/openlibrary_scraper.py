import requests

class OpenLibraryScraper:

    @staticmethod
    def search(query: str):
        url = f"https://openlibrary.org/search.json?q={query}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            books = [{"title": doc.get("title"), "author": doc.get("author_name", [])} for doc in data.get("docs", [])]
            return books
        return []
