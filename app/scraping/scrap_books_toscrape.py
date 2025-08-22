import requests
from bs4 import BeautifulSoup

class BooksToScrape:

    @staticmethod
    def search(query: str):
        results = []
        for page in range(1, 3):  # 2 pages pour l'exemple
            url = f"http://books.toscrape.com/catalogue/page-{page}.html"
            response = requests.get(url)
            if response.status_code != 200:
                continue
            soup = BeautifulSoup(response.text, 'html.parser')
            for book in soup.select('h3 a'):
                title = book.attrs['title']
                if query.lower() in title.lower():
                    results.append({"title": title})
        return results
