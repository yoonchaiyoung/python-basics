numbers = [1, 2, 3, 4, 5, 6, 7, 8]
results = []

# 리스트 함축(list comprehension)
# Syntax : [값연산식 for 객체 in 순차형 if 조건문]

# numbers 순차형의 모든 내부 요소를 제곱해보자.
for n in numbers:
    result = n * n
    results.append(result)

print(results)

results = [num*num for num in numbers]
print(results)

# 두 개 결과 동일함

# 문자열 리스트에서 길이가 2이하인 문자열만 새로운 리스트에 담기
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
results = []
for s in strings:
    if len(s) <= 2:
        results.append(s)

print(results)

results = [s for s in strings]
print(results)

results = [s for s in strings if len(s) <= 2]
print(results)


# 1 ~ 100 사이의 수 중에 짝수 리스트 만들기
results = [n for n in range(1, 101) if n % 2 == 0]
print(results)


# 문자열 리스트에서 각각의 문자열의 길이를 담은 리스트 만들기
results = [len(s) for s in strings]
print(results)

# 1 ~ 100 사이의 숫자 중 일의 자리가 3인 것만 있는 리스트
# [3, 6, 9, 13, 16, 19, 23, 26, 29, 30, 31, 33, 36,,,,,,,]
results = [number for number in range(1, 101) if str(number).count('3')>0
           or str(number).count('6')>0
           or str(number).count('9') >0]
print(results)

# set comprehension
# Syntax : {값연산식 for 객체 in 순차형 if 조건문}
s = {s for s in strings if len(s) <= 2}
print(s)

# dict comprehension
# Syntax : {키연산식:값연산식 for 객체 in 순차형 if 조건문}
d = {s : len(s) for s in strings}
print(d)










