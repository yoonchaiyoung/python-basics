# 생성
# s = {}    # set 아님. dict 임.
s = set()   # 빈 set. 빈 집합.
s = {1, 2, 3}
# 수학에서 이야기하는 집합이랑 똑같음
print(s, type(s))
# 집합 : 순서 X, 중복허용 X, 인덱싱&슬라이싱 X

# 기본 연산
print(len(s))
print(2 in s)
print(10 not in s)

# list 중복성을 제거할 수 있다.
l = {1, 2, 3, 4, 2, 2, 5, 6, 5, 6}
s2 = set(l)
print(s2)
# 출력결과 : {1, 2, 3, 4, 5, 6}


print("============== 객체함수 =================")
s3 = set()
# {} 그냥 이렇게 하면 dictionary 랑 표기가 똑같아서 dictionary를 만들어버림.
# 텅 빈 set을 만들려면 set() 라고 하기.
s3.add(7)
print(s3)

s3.add(2)
print(s3)

s3.discard(2)
print(s3)

# s3.remove(10)
# 출력결과 : Process finished with exit code 1
# 예외 발생.


try:
    s3.remove(10)
except KeyError as e:
    print('remove는 discard와 다르게 존재하지 않는 요소 제거시 예외가 발생')

s3.remove(7)
print(s3)

s.update({2, 4, 6}) # 이미 있는 키는 추가되지 않음
print(s3)

# add 해도 요소를 넣을 수 있지만 많은 요소를 넣고 싶을 대는 update 이용하면 편리함

s3.clear()
print(s3)


# 수학의 집합과 관련된 함수
s4 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s5 = {10, 20, 30}

# 합집합
s6 = s4.union(s5)
print(s6)
# 합집합 연산자 (|)
print(s4, "합집합", s5, "=", s4 | s5)

# 교집합
s7 = s4.intersection(s5)
print(s7)
# 교집합 연산자 (&)
print(s4, "교집합", s5, "=", s4 & s5)

# 차집합
s8 = s4.difference(s5)
print(s8)
# 차집합 연산자 (-)
print(s4, "차집합", s5, "=", s4 - s5)

# 대칭차집합
s9 = s5.symmetric_difference(s5)
print(s9)

# 집합 판별 함수
numbers = { 1, 2, 3, 4, 5, 6, 7, 8, 9}
odds = { 1, 3, 5, 7, 9 }

#   모집합의 확인 issuperset
print(numbers, "는", odds, "의 모집합?", numbers.issuperset(odds))
# 부분집합의 확인 issubset
print(odds, "는", numbers, "의 부분집합?", odds.issubset(numbers))