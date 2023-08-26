import os

파일들 = os.listdir('PYTHON-STUDY')  #거기 있는 파일명들 다 알려주셈
os.rename() #파일 이름 바꾸기

for i in os.listdir('PYTHON-STUDY'):
    os.rename(f'PYTHON-STUDY/{i}',f'PYTHON-STUDY/a{i}')

import shutil # 파일 복사

shutil.copy('파일명','파일명')


