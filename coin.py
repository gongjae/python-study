import json
import requests
import time

data = requests.get('https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/ETH?lastDt=1686276000000&interval=1H&1692754159358')
# print(data.content)

딕셔너리 = json.loads(data.content)
print(딕셔너리['body']['candles'][0]['close'])

#딕셔너리에서 뽑을땐 자료의 이름, 리스트에서 뽑을땐 숫자로 인덱싱
for i in range(200):
    print(딕셔너리['body']['candles'][i]['dt'])
    print(딕셔너리['body']['candles'][i]['close'])
a =time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1685556000000/1000))
print(a)

# epoch 타임: 1970 1월 1일부터 지금까지 몇초나 흘렀는지 초단위로 알려주는 시간형식
for i in range(200):
    #print(딕셔너리['body']['candles'][i]['dt'])
    시간 = 딕셔너리 ['body']['candles'][i]['dt']
    글자시간 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(시간/1000))

    print(글자시간)
    print(딕셔너리['body']['candles'][i]['close'])