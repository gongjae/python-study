중고차 = ['K5', 'white', [5000,6000]]
(중고차[2][0]) = 10000
print(중고차[2][0])

중고차재고 = ['K5','BMW','Tico']
if 'BMW' in 중고차재고:
    print('지금 주문 가능합니다~')

재고량 = 0
if 재고량 > 0:
    print('지금 주문 가능합니다~')
else:
    print('재고량이 없네요 주문 불가능함 ㅅㄱ')
    
for i in range(0,10):
    print('BMW 있어요 사셈')

중고차들 = ['K5','BMW','Tico']
for i in 중고차들:
    print(i)

def 인사하기():
    print('안녕하세요')
    print('잘부탁드려요')

인사하기()

def 모자(숫자):
    print(숫자 + 2)

모자(4)
모자(6)

def 수학연산(x):
    return x + 2
결과 = 수학연산(4)
print(결과)
