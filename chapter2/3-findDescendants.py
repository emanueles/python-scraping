import requests
from bs4 import BeautifulSoup

html = requests.get("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.content, "html.parser")

for child in bsObj.find("table",{"id":"giftList"}).children:
    print(child)