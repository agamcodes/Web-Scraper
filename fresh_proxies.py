import requests
from bs4 import BeautifulSoup

def get_free_proxies():
    r = requests.get("https://free-proxy-list.net/")
    soup = BeautifulSoup(r.text, "html.parser")
    proxies = []
    for row in soup.select("table tbody tr"):
        cols = row.find_all("td")
        if cols[4].text == "elite proxy" and cols[6].text == "yes":
            proxies.append(f"{cols[0].text}:{cols[1].text}")
    return proxies

proxies = get_free_proxies()
print(proxies)