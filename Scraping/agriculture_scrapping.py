import requests
from bs4 import BeautifulSoup


# Function to scrape data from a single page
def scrape_page(page_num):
    url = f"https://baseconnect.in/companies/category/6eb8795f-3ad2-48dd-a91f-200f97752f2d?page={page_num}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    company_names = soup.find_all("a", class_="company-name")
    for company_name in company_names:
        print(company_name.text)


# Scrape data from page 1 to page 150
for page_num in range(0, 1):
    scrape_page(page_num)
