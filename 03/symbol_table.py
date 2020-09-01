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

print("============= Object Symbol Table =================")



g_f.n = 'hello'
g_f.i = 10
print(g_f.__dict__)











