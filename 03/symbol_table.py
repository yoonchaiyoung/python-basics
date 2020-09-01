# global, local 심벌테이블 확인
g_a = 1
g_s = '마이콜'


def g_f():
    l_a = 2
    # g_a = 3
    l_s = '둘리'
    print(g_a) # g_a가 global, local 둘다에 있어서 헷갈려함..
                # scope 우선순위 규칙 : globla에서 찾고 없으면 local 에서 찾고 없으면 built-in(내장)에서 찾음
    # g_a = 2   # 이건 local 에 만드는 것
    a = 2
    print(locals())


print("============= Global Symbol Table VS Local Symbol Table=================")
print(globals())
# 내가 만든 변수 g_a, g_s 변수 맨뒤에 적힘
# 이름이 symbol table 안에 생김

# g_f 는 함수이다. 하고 뒤에 주소 적혀있음.
g_f()

print(g_a)
# print(l_a)        # 에러
                    # local symbol table 은 함수가 실행이 끝나면 사라진다.

print("============= Object's Symbol Table =================")

# 객체.__dict__ : 객체의 symbol table 출력

# 1. 사용자 정의 함수
# 심벌테이블 O -> 확장 O
# 우리가 직접 만든 함수는 symbol table 있음.
# 확장 가능.
g_f.n = 'hello'
g_f.i = 10
print(g_f.__dict__)


# 2. 사용자 정의 클래스
# 심벌테이블 O -> 확장 O
# 클래스, 함수 자체가 객체.
# 그 객체를 tamplet 으로 해서 또 객체를 만들 수 있음.
class MyClass:
    def __init__(self):
        self.i = 10
        self.j = 20
    x = 10
    y = 10

MyClass.z - 10


print(MyClass.__dict__)
# 출력값중에 'x': 10, 'y': 10 있음

MyClass.z = 10
print(MyClass.__dict__)
# 'z': 10 새로 생김


# 3. 내장함수
# 심벌테이블 X -> 확장 X

# print(print.__dict__)
# 에러남.
# __dict__ 라는 속성 없는데?

# print.z = 10
# print(print.__dict__)
# 이런식으로 확장 불가능.


# 4. 내장 클래스
# 심벌테이블 O -> 확장 X
# str.z = 10
print(str.__dict__)


# 5. 사용자 정의 클래스로 생성된 객체
# 심벌테이블 O -> 확장 O
o = MyClass()
print(o.__dict__)
# class MyClass:
#     x = 10
#     y = 10
# 그냥 이렇게 해놓으면 출력값 : {}
# 자기 안에서 돌 수 잇게
# MyClass 에 self 를 추가해줘야지 출력값 : {'i': 10, 'j': 20}

o.k = 30
print(o.__dict__)


# 6. 내장 클래스로 생성된 객체
# 심벌테이블 X -> 확장 X
# 위의 g_a = 1, g_s = '마이콜' 이것도 내장 클래스로 생성된 객체
# print(g_a.__dict__)
# 에러
# g_a.z = 10
# print(g_a.__dict__)
# 에러

# 내장 클래스가 심벌테이블이 있는 거


# 확장이 된다? 심벌테이블이 있다.
# 심벌테이블이 있는데 확장이 될수도/안될수도





















