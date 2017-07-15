# Fetching Table

import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:35729/table.html"
source_code = requests.get(url).text

soup = BeautifulSoup(source_code, "html5lib")

table = soup.find("table")

heading = [th.get_text() for th in table.find("tr").find_all("th")]

data_sets = []

for row in table.find_all("tr")[1:]:
    data_set = zip(heading, (td.get_text() for td in row.find_all("td")))
    data_sets.append(data_set)

for data_set in data_sets:
    print("## Data ##")
    for field in data_set:
        print("{0}: {1}".format(field[0], field[1]))
