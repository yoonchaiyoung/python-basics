# 문제2. 키보드로 정수 수치를 입력 받아 짝수인지 홀수 인지 판별하는 코드를 작성하세요.

# while True:
#     print('--------')


number = int(input('수를 입력하세요:'))
if number % 2 == 1:
    print('홀수')
else:
    print('짝수')
