import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from pprint import pprint

s = requests.Session()
s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " \
                          "(KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"


# Funksioni merr te gjitha format ne URL-in e caktuar permes librarive requests dhe beautifulSoup
# s.get(url).content kthen response per request tone, dhe funksioni bs ben html parse te permbajtjes
def get_all_forms(url):
    soup = bs(s.get(url).content, "html.parser")
    return soup.find_all("form")
