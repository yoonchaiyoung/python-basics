# 문제1. 파이썬 경로명 s = '/usr/local/bin/python' 에서
# 1) 각각의 디렉토리 경로명을 분리하여 출력하세요.
#
# 실행 결과:
# ‘usr’, ‘local’, ‘bin’, ‘python’
#
# 2) 또, 디렉토리 경로명과 파일명을 분리하여 출력하세요.

# 실행 결과:
#
# ‘/usr/local/‘bin’, ‘python’

# split 함수 사용
# =================================================================================================================
# 1)
s = '/usr/local/bin/python'
s1 = s.split('/')
for i in range(1, 4):
    print("'" + s1[i] + "'", end=', ')
print("'"+s1[-1]+"'")

# 2)
s = '/usr/local/bin/python'
last_slash_index = 0
for i in range(len(s)):
    if s[i] == '/':
        last_slash_index = i
print(last_slash_index)

s1 = ''
s2 = ''
for j in range(len(s)):
    if j < last_slash_index:
        s1 = s1 + str(s[j])
    elif j > last_slash_index:
        s2 = s2 + str(s[j])
print("'"+s1+"', '"+s2+"'")