#class/object 문법
#게임 정보제공 사이트를 만들고 싶다 - 그럼 캐릭마다 정보를 자료형으로 정리

# dictionary 복사로도 쉽게 구현이 가능한가? NO
garen = nunu
캐릭2 = nunu
캐릭3 = nunu
#nunu = {
#   'q':'eat',
#  'w':'snowball'
#   }
#garan = {
#   'q':'strike',
#  'w':'courage'
# }

#오브젝트 만드는 문법
#오브젝트.q = 'eat'
#오브젝트.w = 'snowball'

#오브젝트 한줄컷 생산해주는 기계
#class 에서 object 뽑을때 def __init__ 실행됨
#self는 새로 생성될 object를 뜻함
class Hero:
   def __init__(self,구멍):
      self.q= 구멍
      self.w = 'snowball'

   def hello(self):
      print('안녕하세요')

nunu = Hero('eat')
garan = Hero('strike')
print(nunu.q)
print(garan.q)
nunu.hello()

