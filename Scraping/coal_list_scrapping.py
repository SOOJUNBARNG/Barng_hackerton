import requests
from lxml import html
import csv
import time

# URL of the website
urls = [
    "https://baseconnect.in/companies/keyword/e33221e8-bf9b-42f9-aed0-346243ebee26",
    "https://baseconnect.in/companies/keyword/e33221e8-bf9b-42f9-aed0-346243ebee26?page=2",
]


# Create a session
session = requests.Session()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}


def safe_cp932(text):
    try:
        return text.encode("cp932", errors="replace").decode("cp932")
    except UnicodeEncodeError:
        return "Encoding Error"


# Open a CSV file in write mode
with open(
    r"C:\Users\staff\Documents\Bakuchu\coal=organizations_data.csv", "w", newline="", encoding="cp932"
) as csvfile:
    writer = csv.writer(csvfile)

    # Write headers
    writer.writerow(["Organization Name", "detail", "detail_explain"])

    for url in urls:
        try:
            print(f"Scraping: {url}")
            # Send a GET request to the website
            response = session.get(url, headers=headers)
            response.raise_for_status()  # Check that the request was successful

            # Parse the HTML content with lxml
            tree = html.fromstring(response.content)

            for i in range(0, 100):
                org_name = tree.xpath("/html/body/section/div[1]/div[4]/div[2]/div[" + str(i) + "]/h3/a/text()")
                detail = tree.xpath("/html/body/section/div[1]/div[4]/div[" + str(i) + "]/div[2]/div[2]/h5/text()")
                detail_explain = tree.xpath(
                    "/html/body/section/div[1]/div[4]/div[" + str(i) + "]/div[2]/div[2]/p[1]/text()"
                )

                # Convert lists to strings and strip extra whitespace
                org_name = org_name[0].strip() if org_name else "N/A"
                print(org_name)
                detail = detail[0].strip() if detail else "N/A"
                detail_explain = detail_explain[0].strip() if detail_explain else "N/A"

                org_name = safe_cp932(org_name)
                detail = safe_cp932(detail)
                detail_explain = safe_cp932(detail_explain)

                writer.writerow([org_name, detail, detail_explain])

            # Delay to avoid overwhelming the server
            time.sleep(2)

        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except Exception as err:
            print(f"An error occurred: {err}")
