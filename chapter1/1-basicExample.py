import requests
html = requests.get("http://www.pythonscraping.com/exercises/exercise1.html")
print(html.content)