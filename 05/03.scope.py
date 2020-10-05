def func1(a):
    x = 10          # 할당 작업 -> 로컬 심볼 테이블에 생성
    return a * x


def func2(a):
    return a + x    # x는 할당이 일어나지 않음 -> Global 영역의 x를 참조


# def func3(a):
#     return a + y


x = 1
g = 10

# (L)GB
r = func1(10)
print(r)
print(x)

# (L)GB
r = func2(10)
print(r)

# LG(B)
print(dir())
print(dir('__builtins__'))
# r = func3(10)
# print(r)
# 에러
# y가 없음.
# y가 L,G,B 전부에 없다.

def func3(a):
    global g            # local 변수를 새로 만드는 것이 아닌
                        # global 변수를 가져다 쓰겠다.
    g = 3
    return a + g

# global 키워드
r = func3(10)
print(r)
