import requests
from bs4 import BeautifulSoup

def scrape_books():
    # Practice site for web scraping
    url = "http://books.toscrape.com/"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        # Saari books ek 'article' tag mein hoti hain
        books = soup.find_all("article", class_="product_pod")

        print(f"🎯 Found {len(books)} books on this page!\n")

        for book in books:
            # Title nikalna
            title = book.h3.a["title"]
            
            # Price nikalna
            price = book.find("p", class_="price_color").get_text()
            
            # Availability (Stock mein hai ya nahi)
            stock = book.find("p", class_="instock availability").get_text().strip()

            print(f"Title: {title}")
            print(f"Price: {price}")
            print(f"Status: {stock}")
            print("-" * 30)

    except Exception as e:
        print(f"Error aa gaya: {e}")

# Run the function
scrape_books()
