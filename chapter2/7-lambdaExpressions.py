import requests
from bs4 import BeautifulSoup
html = requests.get("http://www.pythonscraping.com/pages/page2.html")
bsObj = BeautifulSoup(html.content, "html.parser")
tags = bsObj.findAll(lambda tag: len(tag.attrs) == 2)
for tag in tags:
	print(tag)