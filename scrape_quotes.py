import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://quotes.toscrape.com"

# Send request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all quote blocks
quotes = soup.find_all("div", class_="quote")

data = []

for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text

    data.append({
        "Quote": text,
        "Author": author
    })

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("quotes_data.csv", index=False)

print("Web scraping completed successfully!")
