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





def scan_sql_injection(url):
    for c in "\"'":
        new_url = f"{url}{c}"
        res = s.get(new_url)
        if is_vulnerable(res):
            return True
            return
    # Test ne HTML forms
    forms = get_all_forms(url)
    for form in forms:
        form_details = get_form_details(form)
        for c in "\"'":
            data = {}
            for input_tag in form_details["inputs"]:
                if input_tag["value"] or input_tag["type"] == "hidden":
                    try:
                        data[input_tag["name"]] = input_tag["value"] + c
                    except:
                        pass
                elif input_tag["type"] != "submit":
                    data[input_tag["name"]] = f"test{c}"
            url = urljoin(url, form_details["action"])
            if form_details["method"] == "post":
                res = s.post(url, data=data)
            elif form_details["method"] == "get":
                res = s.get(url, params=data)
            if is_vulnerable(res):
                return True
                break
    return False


