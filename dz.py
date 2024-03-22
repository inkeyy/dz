import requests
from bs4 import BeautifulSoup

url = 'https://stopgame.ru/'
responce = requests.get(url)
print(responce.status_code)

soup = BeautifulSoup(responce.text, "html.parser")
print(soup.a.get("href"))

a_tags = soup.find_all("a")
for a_tags in a_tags:
    print(a_tags)

img_tags = soup.find_all("img")
for img_tags in img_tags:
    print(img_tags)

title_tags = soup.find_all("title")
for title_tags in title_tags:
    print(title_tags)

li_tags = soup.find_all("li")
for li_tags in li_tags:
    print(li_tags)

p_tags = soup.find_all("p")
for p_tags in p_tags:
    print(p_tags)

h_tags = soup.find_all("h3")
for h_tags in h_tags:
    print(h_tags)

