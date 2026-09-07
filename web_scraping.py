import requests
from bs4 import BeautifulSoup
import pandas as pd

books = []

for page in range(1, 6):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    for book in soup.select("article.product_pod"):
        title = book.h3.a["title"]
        price = book.select_one(".price_color").get_text(strip=True)
        availability = book.select_one(".availability").get_text(" ", strip=True)
        rating = book.select_one("p.star-rating")["class"][1]

        relative_url = book.h3.a["href"]
        product_url = "https://books.toscrape.com/catalogue/" + relative_url

        books.append({
            "Title": title,
            "Price": price,
            "Availability": availability,
            "Rating": rating,
            "URL": product_url
        })

df = pd.DataFrame(books)

df.to_csv("books_data.csv", index=False)

print("Total books:", len(df))
print(df.head())
