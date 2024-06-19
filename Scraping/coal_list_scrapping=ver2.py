import requests
from bs4 import BeautifulSoup
from lxml import html
import csv

# Create a session
session = requests.Session()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
# URL of the website
urls = [
    "https://baseconnect.in/companies/keyword/e33221e8-bf9b-42f9-aed0-346243ebee26",
    "https://baseconnect.in/companies/keyword/e33221e8-bf9b-42f9-aed0-346243ebee26?page=2",
]


# Open a CSV file in write mode
with open(
    r"C:\Users\staff\Documents\Bakuchu\coal=organizations_data.csv", "w", newline="", encoding="cp932"
) as csvfile:
    writer = csv.writer(csvfile)

    # Write headers
    writer.writerow(["Organization Name"])

    for url in urls:
        try:
            # Send a GET request to the website
            response = session.get(url, headers=headers)
            response.raise_for_status()  # Check that the request was successful

            # レスポンスのエンコーディングを確認
            response.encoding = response.apparent_encoding
            soup = BeautifulSoup(response.text, "html.parser")
            # soup = soup.prettify()

            h3s = soup.find_all("h3")
            for h3 in h3s:

                org_name = h3.get_text()
                writer.writerow([org_name])

        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except Exception as err:
            print(f"An error occurred: {err}")
