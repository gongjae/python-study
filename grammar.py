#현재시간 출력하는 법
import time
print(time.time())

#처리시간이 오래걸리는 코드
10000000000 + 1222222222222222222
a = time.time()
b =time.time()
print(b -a)

#현재 ctime 출력하는 법
시간 = time.time()
시간 = time.ctime(시간)
print(시간)

#localtime()으로 세부 항목만 출력하기   
시간 = time.localtime()
print('현재 시간은' + str(시간.tm_hour))

#strftime()으로 시간표시형식 맘대로 바꾸기
print(time.strftime('%Y year %m month',시간))

#문자 formating
name = 'Kim'
print('안녕하세요 %s'%name)
print(f'안녕하세요{name}')

#시간 출력하고 싶은데 복잡한 생각 싫으면
import datetime
print(datetime.datetime(2022, 10, 1))

