from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import time 


# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get('https://instagram.com')


time.sleep(3)
e = driver.find_element(By.CSS_SELECTOR,'<input aria-label="전화번호, 사용자 이름 또는 이메일" aria-required="true" autocapitalize="off" autocorrect="off" maxlength="75" class="_aa4b _add6 _ac4d" dir type="text" value name="username">')
e.send_keys('codingapple_test')
e = driver.find_element(By.CSS_SELECTOR,'<input aria-label="비밀번호" aria-required="true" autocapitalize="off" autocorrect="off" class="_aa4b _add6 _ac4d" type="password" value name="password">')
e.send_keys('qwer1234%')
e.send_keys(By.ENTER)
