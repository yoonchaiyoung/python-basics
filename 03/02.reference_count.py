import sys

x = object()
print(type(x))
print(sys.getrefcount(x))
# 출력값 : 2
# x에서 1번 참조, getrefcount 함수에서 1번 참조
# 총 2번 참조

y = x
print(sys.getrefcount(x))
print(globals())

# reference 값 줄이기
del x
# print(sys.getrefcount(x))
# x 지웠으니까 에러

print(sys.getrefcount(y))
print(globals())
# 심벌테이블에서 x 자체가 사라짐

# y까지 없애버리면 참조했던 객체는 사라짐(garbage collection)