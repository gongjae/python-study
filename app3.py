import requests
from bs4 import BeautifulSoup

def 현재가(구멍):
    데이터 = requests.get(f'https://finance.naver.com/item/sise.nhn?code={구멍}')
    soup = BeautifulSoup(데이터.content, 'html.parser')
    print(soup.find_all('strong',id="_nowVal")[0].text)
    print(soup.find_all('span',class_="tah")[5].text)
    return soup.find_all('strong',id="_nowVal")[0].text
현재가('005930')
현재가('066575')

f = open('a.txt','w')
f.write(현재가('005930'))
f.write(현재가('066575'))
f.close()


# soup.select('.tah')  
# soup.select('#tah')  
# soup.select('.f_down em')
# 이미지 = soup.select('#img_chart_area')
# print(이미지['src'])

