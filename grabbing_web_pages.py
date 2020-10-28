import requests
from pprint import pprint

# URL = "https://www.accenture.com/us-en"

# response = requests.get(URL)
#
# if response.status_code == requests.codes.OK:
#     page_content = response.content.decode()
#     print(page_content)

URL = "http://localhost:8000/api/artists"

response = requests.get(URL, params={"birthplace": "london"})  # data={}, auth=(user, pw), headers={}, proxy={} ...
if response.status_code == requests.codes.OK:
    data = response.json()
    pprint(data)

