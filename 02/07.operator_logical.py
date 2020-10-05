# 일반적으로 피연산자(operand)는 True 또는 False 값을 가지는 연산
a = 20
print(a < 20)

# not T = F
print(not a < 20)

# T and T = T
# T and F = F
# F and T = F
# F and F = F
print(a < 30 and a != 30)

# T or T = T
# T or F = T
# F or T = T
# F or F = F
print(a == 30 or a > 30)


# 논리식의 계산순서
# Circuit Break
print(True or 'logical')
print(True or bool('logical'))
# 위에거 2개는
# 앞부분자체가 True 인데 or 이니까 어쨋든 결과가 True이니까 뒤를 실행을 안해버림
print(False or 'logical') # 앞부분 : False인데 or 이니까 뒷부분도 판단해야함. 그래서 logical 이라고 출력함
print([] or 'logical') # 앞부분 : False
print([] and 'logical') # 앞부분 : False, and니까 어쨌든 결과는 False니까 앞부분 출력
print([2,10] and 'logical') # 앞부분 : True, and니까 뒷부분 판단해야함. 그래서 logical 출력


def f():
    print('hello world')

a > 10 and f() # True, and, 뒷부분판단, hello world 출력
a > 10 or f()
# 위의 코드와 동일한 것은
# 바로 아래 코드 if문
if a > 10:
    f()

s = 'Hello World'
s and print(s)



