# 문제5.
# 함수 sum 을 만드세요. 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산합니다.

#
# <<실행결과>>
#
# 0
# 3
# 18
#
# (교수님)
# def sum
#
#
# print(sum())
# print(sum(1, 2))
# print(sum(1, 2, 5, 7, 2, 3))
#
# 가변 인자
# 한번
# 사용해보라는
# 얘기
# =================================================================================================================
def sum(*args):
    sum1 = 0
    for i in range(len(args)):
        sum1 += args[i]
    return sum1

print(sum())
print(sum(1, 2))
print(sum(1, 2, 5, 7, 2, 3))
