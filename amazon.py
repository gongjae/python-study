import requests

헤더스 = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36']

쿠키 =['aws-target-data:%7B%22support%22%3A%221%22%7D', 'regStatus:pre-register' 'aws-target-visitor-id:1684292395282-29432.32_0', 'AMCV_7742037254C95E840A4C98A6%40AdobeOrg:1585540135%7CMCIDTS%7C19499%7CMCMID%7C83769012074727160182693592338109232172%7CMCAAMLH-1685256664%7C11%7CMCAAMB-1685256664%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1684659064s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0', 'csm-sid:340-2401061-1150799', 'x-amz-captcha-1:1693045859815988', 'x-amz-captcha-2:9CsX1loFeVfnjK5sEhvWng::', 'session-id:136-3791813-6368822', 'session-id-time:2082787201l', 'i18n-prefs:USD', 'sp-cdn:"L5Z9:KR"', 'skin:noskin', 'ubid-main=135-9148643-3145249; csm-hit=tb:s-0ECD8V2PF9E720R9JBWQ|1693038891826&t:1693038892611&adb:adblk_no', 'session-token:9b/E0i4xXebdMPHqs//LdWHqcpD3ZiJraD/4a/X0Jta48KiSOT96D9hz+SzCuXuX7kv5ydXcfJz0sUgm22GQcSCKdTsiP9eHNm3NmfH60sztghXCoeqZi+p6QK77MXqJMw39HXamCTbm+NJWzJzudZkaxVCr25qXqJXr5DFjlTgQumnyz7NfwDX+BZ9nplSEDRrLPJlLuWSSxglmIjSC1dDnwcErufiRBQnHxzw+XRy/wWjHBQ5Z66McgvEqUzxsWapF+RicZphz+PXd2ePRRmuJb1WqpgMhnNMLnwfZU4YXKhV01VQSQluew5jSg+2jMKpQxhkuM6hjLrFHEQtx0Kb02m4OHMdE']

r =requests.get('https://www.amazon.com/s?k=monitor&crid=1AJC4SODF83K3&sprefix=monitoi%2Caps%2C373&ref=nb_sb_noss_2',headers=헤더스, cookies=쿠키)

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.content,'lxml')
print(soup.select('.a-size-medium')[0])

#에러코드 
if r.status_code ==200:
    print(soup.select('.a-size-medium')[0])
else:
    print('에러났어요')

#에러나서 코드가 멈추는 것 예방
try:
    print(soup.select('.a-size-medium')[110]) #이거 해보고
except:
    print('안되네요') #혹시 에러뜨면 이거해봐