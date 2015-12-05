import requests
from bs4 import BeautifulSoup

html = requests.get("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.content, "html.parser")
print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())