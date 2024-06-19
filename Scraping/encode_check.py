import requests
from bs4 import BeautifulSoup
from lxml import html

# Create a session
session = requests.Session()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
url = "https://baseconnect.in/companies/keyword/e33221e8-bf9b-42f9-aed0-346243ebee26"

# Send a GET request to the website
response = session.get(url, headers=headers)
response.raise_for_status()  # Check that the request was successful

# レスポンスのエンコーディングを確認
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text, "html.parser")
# soup = soup.prettify()

# paragraphs = soup.find_all("searches__result__list__conts__text__heading")
# for p in paragraphs:
#     print(p.get_text())

h3s = soup.find_all("h3")
for h3 in h3s:
    print(h3.get_text())
