import requests
from bs4 import BeautifulSoup

html = requests.get("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html.content, "html.parser")
nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text())