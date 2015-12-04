import requests
from bs4 import BeautifulSoup


html = requests.get("http://www.pythonscraping.com/exercises/exercise1.html")
bsObj = BeautifulSoup(html.content, "html.parser");
print(bsObj.h1)