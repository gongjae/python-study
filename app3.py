import requests
from bs4 import BeautifulSoup

데이터 = requests.get('https://finance.naver.com/item/sise.nhn?code=005930')

soup = BeautifulSoup(데이터.content, 'html.parser')
print(soup.find_all('strong',id="_nowVal")[0].text)
print(soup.find_all('span',class_="tah")[4].text)
soup.select('.tah') 
soup.select('#tah') 
soup.select('.f_down em')
이미지 = soup.select('#img_chart_area')
print(이미지['src'])

