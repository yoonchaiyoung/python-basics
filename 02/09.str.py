
# 한 줄 문자열
s = ''
str1 = 'Hello World'
str2 = "Hello World"
print(type(s), type(str1), type(str2))
print(isinstance(str1, str))

# 여러줄 문자열
str3 = '''ABC
DEF
가나다라마바사
아자차카타파하'''
print(str3)

# 여러줄 주석 -> 여러줄 문자열
'''
주석1
주석2
주석3
'''

# escape

print('hello\nword\n')
print('hello "world"')
print('She\'s Mom')
print("She's Mom")
print("둘리\t010-0000-0000")

print('====== 문자열 연산 ======')
s1 = 'First String'
s2 = 'Second String'

# str 역시 순차자료형의 특징을 가지고 있다.
# 불변 객체 -> 내부 값은 변경할 수 없다.
s3 = s1*3
print(s3)

# +(연결, concatenate)
temp = ' '
s4 = s1 + temp + s2
print(s4)
print(s1 + ' ' + s2)

s5 = 'Hello' '-' 'world' # 생략가능하다.
s6 = 'Hello' + '-' + 'world'
print(s5)
print(s6)


# 문자열 객체와 정수 객체는 연결(+) 연산을 할 수 없다.
# 예외 : 발생
# print("hello" + 2)    # Error
print("hello" + str(2))



# 인덱싱(sequence 타입이 가지는 특징)
# 앞에서부터는 0 1 2...
# 맨뒤부터는 -1 -2 -3...

print(s3[0], s2[1], s1[2]) # 정방향 indexing
print(s1[-11], s1[-10], s1[-9]) # 역방향 indexing


# slicing(sequence 타입이 가지는 특징)
s7 = s1[2:5]        # [시작:끝경계:간격]
print(s7)           # rst
print(s1[-10:-7])   # 음수 인덱스를 이용한 슬라이싱
print(s7 == s1[-10:-7])
print(s1[2:12])
print(s1[2:])       # == s1[2:len(s1)] -> 생략하면 끝까지

# 슬라이시으이 세 번째 값은 간격값 ( 기본 : 1)
print("간격 2:", s1[::2])     # 처음부터 끝까지 간격을 2로
                             # == s1[0:len(s1):2]
                             # 간격값이 음수면 방향 반대
print("간격 -1:", s1[::-1])


# len()함수(sequence 타입이 가지는 특징)
print(len(s1))


# in, not in 연산자(sequence 타입이 가지는 특징)
print("s" in s2)
print("s" not in s2)

print('====== 포맷팅 ======')

# tuple
f = "name: %s, age: %d"
print(f)

print(f %('둘리', 10))
print("name: %s, age: %d" % ('둘리', 10))


# dict
print("name: %(name)s, age: %(age)d" % {'name': '둘리', 'age': 10})



# format() 함수
name = '마이콜'
age = 30
print("name: " + format(name, 's') + ", age: " + format(age, 'd'))

# format() 객체 함수
print("name: {0}, age: {1}".format(name, age))          # numbered placeholder
print("name: {}, age: {}".format(age, name))            # 익명 플레이스 홀더
print("name: {}, age: {}".format(name, age))
print("name: {1}, age: {0}".format(age, name))
# 전역함수, 객체함수 구별해야함..
print("name: {n}, age:{a}".format_map({'n': name, 'a': age}))   # named placeholder
# 사전을 포맷할 때는 format_map 메서드 이용


print('====== 객체함수 ======')
# .으로 접근하는 함수
s8 = 'i like python'
print(s8.upper())
print(s8.lower())
print(s8.swapcase())    # 대문자 <-> 소문자
print(s8.capitalize)    # 첫 글자 : 대문자
                        # 나머지 글자 : 소문자
print(s8.title())       # 각 단어의 첫 글자만 대문자


s9 = 'I Like Python. I Like Java Also'
print(s9.count('Like'))
print(s9.find('Like'))      # 처음부터 검색
print(s9.find('Like', 5))   # 검색범위 제한
print(s9.find('Like', 21))  # 출력값 : -1
                            # 없다. 라는 의미
print(s9.find('JavaScript'))
print(s9.rfind('Like'))
print(s9.startswith('I Like'))
print(s9.startswith('I Like', 2))
# print(s9.endtswith('Also')) # Process finished with exit code 1 : 에러난거임.. 0과 1 return 하는 데 0은 정상작동 1은 에러
print(s9.endswith('Also'))      # 'Also'로 끝나는가?
print(s9.endswith('Java', 0, 26))   # 범위의 제한 [0:26] 구간의 문자열이 'Java'로 끝나는가?

# find와 index : -> 사용법 거의 동일
# find : 예외 발생 없음
# index : 예외 발생 있음

index = s9.find('JavaScript')
if index == -1:
    print('not found')

# 예외처리보다는 로직으로 짜는 것이 더 좋음.
# find 계열의 함수를 찾는 것이 좋음.
# 예외하지마..


# index()는 발견하지 못하면 예외가 발생한다.
try:
    print(s9.rindex('Like'))  # 의심스러운 코드같은 것들은 이 안에 넣어버림
                              # 얘를 s9.index('JavaScript') 보다 위에 놓아야. 만약 밑에 놓으면 s9.index('JavaScript')에서 에러나면 그 아래줄 실행 안하고 ValueError 로 가버리니까..
    s9.index('JavaScript')

except ValueError as ex:
    print('예외처리:' + str(ex))

try:
    s9.index('JavaScript')
    s9.rindex('Like')
except ValueError as ex:
    # 예외
    # 1. 로그(파일)를 남긴다. // 로그를 보면서 오류를 찾는다.
    # pass 라고 해버리면 정상실행이 되버리니까 로그 안 남음
    # 2. 사용자에게 사과.
    # 3. 정상종료 // 예외발생했는 데 더 진행하면 더 무슨 상황이 생길지 모름..
    print('index()는 발견하지 못하면 예외가 발생한다.')

# 예외를 가지고 짜면 예외가 기록에 남아서 안 좋음...
# 예외는 db연결할 때 좋음
# ex) 서버가 켜져있을 거라고 생각했는 데 인터넷이 죽어있거나 할 때 등등
# 이럴때 예외처리를 하는 것이 좋음





# 편집과 치환
# 공백제거(trim)
s10 = '   spam and ham    '
print('-----' + s10.strip() + '------')
# strip 함수 : 양옆의 공백(화이트 스페이스)을 없앤다.

print('-----' + s10.rstrip() + '------')
# rstrip 함수 : 오른쪽의 공백(화이트 스페이스)을 없앤다.
print('-----' + s10.lstrip() + '------')
# lstrip 함수 : 왼쪽의 공백(화이트 스페이스)을 없앤다.

# 기본은 공백을 제거하지만, 특정 문자열을 제거할 수도 있음.
# replace 가 아님

s11 = '<><abc><><defg><>'
print('-----' + s11.strip('<>') + '------')
# 출력결과 : -----abc><><defg------
# 끝에 있는 문자열중에 <랑 >가 있는 거 다 없앰
# 지정한 문자 : < or >
print('-----' + s11.strip('<') + '------')
# 출력결과 : -----><abc><><defg><>------

# 가운데 있는 것까지 없애고 싶거나 다른 문자열로 바꾸고 싶을 때는
# replace 함수 사용
s12 = 'Hello Java Java Java'
print('-----' + s12.strip('Java') + '------')
print('-----' + s12.replace('Java', '') + '------')     # 내부의 검색어('Java')를 다른 문자열로 치환


# 정렬
s13 = 'King and Queen'
print(s13.center(30))
# s13 문자열을 가운데에 놓고 30자가 되도록 양쪽 공백까지 해서 만들어준다.
print('-----' + s13.center(30) + '-----')   # 30자리 확보 후 문자열 가운데 정렬
print('-----' + s13.ljust(30) + '-----')    # 30자리 확보 후 문자열 왼쪽 정렬
print('-----' + s13.rjust(30) + '-----')    # 30자리 확보 후 문자열 오른쪽 정렬


# 분리
# 'GET /index.py HTTP/1.1'
s14 =  'spam and ham'
r = s14.split(' and ')
# 괄호안을 기준으로 분리
# 구분자를 기준으로 문자열을 분절 -> list 반환
print(r, type(r))
# print 함수가 여러개를 출력해야할때는
# 튜플이나 리스트에 담아서

s15 = 'one:two:three:four:'
r = s15.split(':')
print(r)

s15 = 'one:two:three:four'
r = s15.split(':')
print(r)

r = s15.split(':', 2)
print(r)
# 왼쪽 두개, 나머지 -> 3개 요소의 list

r = s15.rsplit(':', 2)
print(r)
# 나머지, 오른쪽 두개 -> 3개 요소의 list

lines = '''1st line
2nd line
3rd line
4th line
'''

r = lines.strip().split('\n')
print(r)
r = lines.split('\n')
print(r)

r = lines.splitlines()      # lines.split('\n')
print(r)
# 빈 문자열을 없애버림.


# 결합
s16 = ''.join(r)        # 문자열을 기준으로 리스트를 연결하여 새 문자열 반환
print(s16)

s16 = '&'.join(r)
print(s16)



# 판별
print("1234".isdigit())
print("abcd".isalpha())
print("1234".isalpha())
print("abcd".isdigit())
print("abcd".islower())
print("abcd".isupper())
print("ABCd".isupper()) # 한개라도 소문자가 있으면 출력값 : False
print(" ".isspace())    # 화이트 스페이스 확인 : 공백, 개행, 탭문자
print("".isspace())
print("\n".isspace())
print("\t".isspace())


# '0' 채우기
number = 234
print(str(number).zfill(5))     # 5자리 빈 공간 확보하고 문자열 세팅 후,
                                # 왼쪽 빈 공간에 0을 채운다.


# str 객체는 변경할 수 없다(불변성, Immutable)
# s10 = 'hello'
# s10[0] = 'f'
# print(s10)
# [cf] list는 변경 가능하다(mutable)
l1 = ['hello', 'world']
print(l1)
l1[0] = 'HELLO'
print(l1)
l1.append('Python')
print(l1)

# docstring

def docstr():
    """
    파이썬은 모듈의 상단,
    클래스, 함수의 선언부 바로 아래 간단한 설명을 적으면
    docstring이 된다"""

# docstring의 확인 : 객체.__doc__
print(docstr.__doc__)
# docstring은 help 함수로도 확인
help(docstr)









# str 객체는 변경할 수 없다(불변성, immutable)
# s10 = 'hello'
# s10[0] = 'f'
# print(s10)

# [cf] list는 변경 가능하다(mutable)
i1 = ['hello', 'world']
print(i1)
i1[0] = 'HELLO'
print(i1)
i1.append('Python')
print(i1)






