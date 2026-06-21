import requests
import time
from fake_useragent import UserAgent
url = "https://mezhdunami.org/"
session = requests.Session()

# headers = {
#     'User-Agent': UserAgent().random,
#     'Accept-Language': 'en-US,en;q=0.9',
#     'Connection': 'keep-alive',
#     'Referer': 'https://www.flipkart.com',
# }

# proxies = {
#     "http": "",
#     "https": ""
# }

time.sleep(2)
r = session.get(url)
#print(r.text)

with open("file.html", "w", encoding="utf-8") as f:
    f.write(r.text)