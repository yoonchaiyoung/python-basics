# 문제1. 키보드로 정수 수치를 입력 받아 그것이 3의 배수인지 판단하세요

# import sys
#
# number = input('수를 입력하세요:')
#
# print(number, type(number))
# number = int(number)
# if number > 10:
#     sys.exit()
#
# print("ok")
#
# number = input('수를 입력하세요:')
# print(number == type(str))

# print(type(str))

judgeNumber = 0
number =  input('수를 입력하세요:')
# 문자열임
# 입력가능한건 : 문자열, 정수, 문자열과 정수열이 같이 있는 경우

for i in number:                                                    # 한글자씩 떼낸다.
    if i not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']: # 숫자인지 본다.
        judgeNumber += 1                                            # 숫자가 아닌게 있다면
    else:                                                           # 숫자라면
        judgeNumber += 0

if judgeNumber != 0:                                                # 숫자가 아닌게 한글자라도 있다면
    print('정수가 아닙니다.')
else:
    if int(number) % 3 == 0:
        print('3의 배수 입니다.')
    else:
        print('3의 배수가 아닙니다.')

# 다른 분 풀이
# number =  input('수를 입력하세요:')
# print(number.isnumeric())
# 숫자면 true
# 숫자가 아니면 false 출력됨.




# 교수님 풀이
# import sys

# number = input('수를 입력하세요:')

# print(number, type(number))
# number = int(number)
# if number > 10:
#     sys.exit()
# print("ok")