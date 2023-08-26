#네이버 로그인 뚫기
#1. 복사 붙여넣기 이용
#2. 실제 브라우저처럼 꾸미기

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import pyperclip

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
옵션 = webdriver.ChromeOptions()
옵션.add_argument(r'user-data-dir=C:\Users\LG\AppData\Local\Google\Chrome\User Data\Default')



driver = webdriver.Chrome(options=옵션)

driver.get('https://nid.naver.com/nidlogin.login?svctype=262144&url=http://m.naver.com/aside/')

time.sleep(2)

pyperclip.copy('아이디')
e = driver.find_element_by_css_selector('#id')
e.send_keys(Keys.CONTROL,'v')

time.sleep(1)

pyperclip.copy('비번')
e = driver.find_element_by_css_selector('#pw')
e.send_keys(Keys.CONTROL,'v')

