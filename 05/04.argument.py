print('======== 기본 인수값 ==========')
# 사용자가 입력을 안 해도 기본값이 들어져가있는 것.
def incr(a, b=1):
    return a * b


# 앞에 값을 기본값으로 할 수 없음. 절대 안 됨.
# def incr(a=1, b):
#     return a + b
# print(incr(10))
# 대입한 10값이 a 꺼인지 b 꺼인지 알 수 없음..


print(incr(10))

print(incr(10, 5))
print(incr(10, b=5))
print(incr(10), end='\n')       # 이게 기본. 바꾸고 싶으면 바꾸면 됨.



print('======== 키워드 인수 ==========')
def area_rect(width, height):
    return width * height


print(area_rect(10, 20))
print(area_rect(width=10, height=20))
print(area_rect(height=20, width=10))
# 인수 명을 명시하여 값을 전달할 수 있다.
# argument 이름(키워드)를 알고 있으면 순서상관없이 넣어도 됨

# print(area_rect(width=10, 20))
# print(area_rect(height=20, 10))
# 둘다 오류
# 키워드 인수 주려면 다 줘야함
# 안 줄거면 순서대로 입력


print('======== 가변 인수 ==========')
def vargs(a, *args):
    print(a, args)
vargs(10)
vargs(10, 20, 30)
# 튜플로 받아버림

# def print(*args, end='\n')
#     pass
# 이거랑 동일


def vargs(a, *args):
    print(a, args)

vargs(10)
vargs(10, 20, 30)
# 첫번재꺼 빼고 튜플로 만들어줌

def _print(*args, end='\n'):
    print(args, end)

_print(10)
_print(10, 20, 30)


def _print(*args, end='newline'):
    print(args)

_print(10)
_print(10, 20, 30)

def _print(*args, end='\n'):
    print(args, end)

_print(10)
_print(10, 20, 30)
_print(10, end='tab')




def _print(*args, sep=' ', end='\n'):
    for c in args:
        print(c, end='')
        print(sep, end='')
    print(end, end='')

print('===================')
print(10, 20, 30, sep=':')
print('===================')
_print(10, 20)
print('===================')
_print(10, 20, 30, sep=':')
print('===================')


print('====== 정의되지 않은 키워드 인수 처리하기 ======')
# 딕셔너리로 들어감
def area(width, height, **args):
    print(width, height)
    print(args)


area(10,20)
area(10, 20, depth=10)
area(10, 20, depth=10, dimension=3)
# area(10, 20, depth=10, 3)
# 에러


def g(a, b, *args, **kw):
    # a, b -> 고정 인수
    # args -> 가변 인수 (list)
    # kw -> 지정되지 않은 키워드 인수(dict)
    print(a, b)
    print(args)
    print(kw)

g(10, 20)                             # 고정 인수 2개
# 출력값 : 10 20
#           ()
#           {}

g(10, 20, 30)                         # 고정 인수 2개, 가변 인수 1개

g(10, 20, c=60)                       # 고정 인수 2개, 키워드 인수 1개

g(10, 20, 30, 40, 50, c = 60, d=70)   # 고정 인수 2개, 가변 인수 3개, 키워드 인수 2개




print('==== 튜플/사전 파라미터 ====')
def h(name, age, height):
    print(name, age, height)

name = '둘리'
age = 10
height = 150
h(name, age, height)

t = ('둘리', 10, 150)
h(t[0], t[1], t[2])
h(*t)
# 결과 똑같음


d = {'name':'둘리', 'age':10, 'height':150}
h(**d)
# 만약
# d = {'name1':'둘리', 'age':10, 'height':150}
# 이런식으로 key 가 잘못 입력되어있으면 에러가 남

# 튜플을 쓸 때는 함수, 파라미터 갯수 맞아야함
# 딕셔너리 쓸 때는 갯수도 맞고 key 이름도 맞아야함

