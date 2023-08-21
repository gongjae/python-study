import requests
from bs4 import BeautifulSoup

데이터 = requests.get('https://dak.gg/')
soup = BeautifulSoup(데이터.content, 'html.parser')

for i in range(14):
    print(soup.find_all('span',class_="dropdown-game-name")[i].text)