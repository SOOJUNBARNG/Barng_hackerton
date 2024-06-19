import requests
from lxml import html
import csv

# URL of the website
urls = [
    # "https://amazing-human.jp/mie-touroku/",
    # "https://amazing-human.jp/fukuoka-touroku/",
    # # "https://amazing-human.jp/okayama-touroku/",
    # "https://amazing-human.jp/tokushima-touroku/",
    # "https://amazing-human.jp/fukui-touroku/",
    # "https://amazing-human.jp/toyama-touroku/",
    # "https://amazing-human.jp/okinawa-touroku/",
    # "https://amazing-human.jp/nagasaki-touroku/",
    # "https://amazing-human.jp/miyazaki-touroku/",
    # "https://amazing-human.jp/kumamoto-touroku-2/",
    # "https://amazing-human.jp/yamaguchi-touroku/",
    # "https://amazing-human.jp/hiroshima-touroku/",
    # "https://amazing-human.jp/shizuoka-touroku/",
    # "https://amazing-human.jp/wakayama-touroku/",
    # # "https://amazing-human.jp/osaka-touroku/",
    # "https://amazing-human.jp/osaka-touroku/2/",
    # # "https://amazing-human.jp/osaka-touroku/3/",
    # "https://amazing-human.jp/osaka-touroku/4/",
    # "https://amazing-human.jp/osaka-touroku/5/",
    # "https://amazing-human.jp/aichi-touroku/",
    # "https://amazing-human.jp/aichi-touroku/2/",
    # "https://amazing-human.jp/aichi-touroku/3/",
    # "https://amazing-human.jp/aichi-touroku/4/",
    # "https://amazing-human.jp/aichi-touroku/5/",
    # "https://amazing-human.jp/aichi-touroku/6/",
    # "https://amazing-human.jp/nara-touroku/",
    # "https://amazing-human.jp/hyogo-touroku/",
    "https://amazing-human.jp/tochigi-touroku/",
    # "https://amazing-human.jp/ibaragi-touroku/",
    # "https://amazing-human.jp/gunma-touroku/",
    "https://amazing-human.jp/chiba-touroku/",
    "https://amazing-human.jp/chiba-touroku/2/",
    "https://amazing-human.jp/kanagawa-touroku/",
    "https://amazing-human.jp/kanagawa-touroku/2/",
    "https://amazing-human.jp/saitama-touroku/",
    "https://amazing-human.jp/saitama-touroku/2/",
    "https://amazing-human.jp/tokyo-touroku/",
    "https://amazing-human.jp/tokyo-touroku/2/",
    # "https://amazing-human.jp/tokyo-touroku/3/",
    "https://amazing-human.jp/tokyo-touroku/4/",
    "https://amazing-human.jp/tokyo-touroku/5/",
    "https://amazing-human.jp/tokyo-touroku/6/",
    "https://amazing-human.jp/tokyo-touroku/7/",
    "https://amazing-human.jp/tokyo-touroku/8/",
    "https://amazing-human.jp/tokyo-touroku/9/",
    "https://amazing-human.jp/tokyo-touroku/10/",
]


# Open a CSV file in write mode
with open(r"C:\Users\staff\Documents\Bakuchu\organizations_data.csv", "w", newline="", encoding="cp932") as csvfile:
    writer = csv.writer(csvfile)

    # Write headers
    writer.writerow(["Organization Name", "Address", "Phone", "Start Date", "URL"])

    for url in urls:
        print(url)
        # Send a GET request to the website
        response = requests.get(url)
        response.raise_for_status()  # Check that the request was successful

        # Parse the HTML content with lxml
        tree = html.fromstring(response.content)

        for i in range(0, 100):
            # article = tree.xpath('//*[@id="top"]/div[4]/main/div/div[1]/section/table[2]/tbody/tr[1]/td/text()')
            org_name = tree.xpath(
                '//*[@id="top"]/div[4]/main/div/div[1]/section/table[' + str(i) + "]/tbody/tr[1]/td/text()"
            )
            address = tree.xpath(
                '//*[@id="top"]/div[4]/main/div/div[1]/section/table[' + str(i) + "]/tbody/tr[2]/td/text()"
            )
            phone = tree.xpath(
                '//*[@id="top"]/div[4]/main/div/div[1]/section/table[' + str(i) + "]/tbody/tr[3]/td/text()"
            )
            start_date = tree.xpath(
                '//*[@id="top"]/div[4]/main/div/div[1]/section/table[' + str(i) + "]/tbody/tr[4]/td/text()"
            )
            url_path = tree.xpath(
                '//*[@id="top"]/div[4]/main/div/div[1]/section/table[' + str(i) + "]/tbody/tr[5]/td/text()"
            )

            # Convert lists to strings and strip extra whitespace
            org_name = org_name[0].strip() if org_name else "N/A"
            address = address[0].strip() if address else "N/A"
            phone = phone[0].strip() if phone else "N/A"
            start_date = start_date[0].strip() if start_date else "N/A"
            url_path = url_path[0].strip() if url_path else "N/A"

            writer.writerow([org_name, address, phone, start_date, url_path])
