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
# Funksioni i cili merr te gjitha detajet e formave te marra nga funksioni i mesiperm
def get_form_details(form):

    # Krijimi i variables te tipit dictionary, qe mbushet me cifte key:value
    details = {}

    # Inicializimi i variables action nga action i formes permes funksionit built-in attrs.get
    try:
        action = form.attrs.get("action").lower()
    except:
        action = None

    # Inicializimi i variables method me metoden get te formes
    method = form.attrs.get("method", "get").lower()

    # Krijimi i vargut inputs ne te cilin fusim te gjitha detajet e nje input-i te formes
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "")
        inputs.append({"type": input_type, "name": input_name, "value": input_value})

    # Ne variablen details fusim {action:"", method:"", inputs:[input_type, input_name, input_value]
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details
