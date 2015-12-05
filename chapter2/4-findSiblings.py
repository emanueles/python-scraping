import requests
from bs4 import BeautifulSoup
html = requests.get("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.content, "html.parser")

for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling) 