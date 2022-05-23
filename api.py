import requests
from pprint import pprint
from bs4 import BeautifulSoup


sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)
# pprint(r.text)

soup = BeautifulSoup(r.text, "html.parser")
print(soup.prettify())
news = soup.find_all(class_="news-title")
print(news[3].text)
