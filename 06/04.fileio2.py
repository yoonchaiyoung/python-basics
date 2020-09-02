f = open('test_t.txt', 'rt', encoding='utf-8')
text = f.read()
print(text)
text = f.read()
print('---' + text + '---')
# 다 읽은 다음에 더 읽으면 아무것도 안 나옴


# position 단위는 byte
pos = f.tell()
print(pos)
# 바이트 단위로 나옴


# 1st Parameter : offset
# 그 위치로부터 얼마나 떨어져 있는 가
# 2nd Parameter : (0:파일의 처음, 1:현재위치, 2:파일의 끝)
f.seek(16, 0)       # 16바이트 이동   # 안녕하세요.까지 포인트 이동함

pos = f.tell()
print(pos)          # 위치 : 16바이트
text = f.read()
print(text)         # 출력결과 : 파이썬입니다.


pos = f.tell()
print(pos)          # read 함수로 끝까지 다 읽었으니까 # 위치 : 37바이트


# line 단위로 읽기
open('fileio2.py', 'rt', encoding='utf-8')



