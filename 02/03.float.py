a = 1.2
print(a, type(a))

# is_integer 함수는 float 객체가 지정한 값으로 정수인지 실수인지 확인이 가능하다.
b = 2
print(type(2))
b = 2.
print(type(b))
b = 2.0
print(type(b))
print(b.is_integer())   # type 은 float 이지만
                        # 실제값은 정수니까 True 라고 나온다.

c = 3e3     # 3*(10**3)
print(c)
d = 0.2e-4
print(d)

