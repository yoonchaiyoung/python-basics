# 문제 4. 구구단 중에 특정 곱셈을 만들고 그 답을 선택하는 프로그램을 작성하는 문제입니다.
# 답을 포함하여 9개의 정수가 아래와 같은 형태로 출력되고 사용자는 답을 골라 입력하게 됩니다.
# 프로그램은 정답 여부를 다시 출력합니다.
#
# 실행 결과:
# 4 X 2 = ?
#
# 18	9	   7
# 63	54	   35
# 8	    28	   81
#
# answer: 8
# 정답
#
# Process finished with exit code 0
#
#(교수님 힌트)
# 사이는 탭으로
#
# 구구단에 있는 값들로만 구성(100넘는 수 안됨)
# 정답이 2개 이상 들어있으면 안됨
# set에 담아서 정답 포함 9개가 나오게끔
# =================================================================================================================
from random import randint

dan1 = randint(1, 9)
dan2 = randint(1, 9)
print("{} x {} = ?".format(dan1, dan2))
print()

answer = dan1 * dan2    # 문제의 정답
set1 = set()     # 중복 방지를 위해 set 이용

i = 0
while len(list(set1)) != 8:
    randNum = randint(1, 9) * randint(1, 9)
    if randNum != answer:
        set1.add(randNum)

randIndex = randint(0, 8)
list1 = list(set1)
list1.insert(randIndex, answer)
print(list1)

for i in range(3):
    for j in range(3):
        print(str(list1[3*i + j]), end='\t')
    print()
print()
guess = int(input("answer : "))
if guess == answer:
    print("정답")
else:
    print("땡!")
