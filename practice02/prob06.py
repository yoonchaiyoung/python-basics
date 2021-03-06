# 문제6
# 숨겨진 카드의 수를 맞추는 게임입니다. 1-100까지의 임의의 수를 가진 카드를 한 장 숨기고 이 카드의 수를 맞추는 게임입니다.
# 아래의 화면과 같이 카드 속의 수가 57인 경우를 보면 수를 맞추는 사람이 40이라고 입력하면 "더 높게",
# 다시 75이라고 입력하면 "더 낮게" 라는 식으로 범위를 좁혀가며 수를 맞추고 있습니다.
# 게임을 반복하기 위해 y/n이라고 묻고 n인 경우 종료됩니다.

# <<실행결과>>
#
# 수를 결정하였습니다. 맞추어 보세요
# 1-100
# 1>>40
# 더 높게
# 2>>50
# 더 높게
# 50-100
# 3>>75
# 50-75
# 4>>64
# 더 낮게
# 50-64
# 5>>55
# 더 높게
# 55-64
# 6>>60
# 더 낮게
# 55-60
# 7>>57
# 맞았습니다.
# 다시 하시겠습니까(y/n)>>n

# (교수님)
# import random
#
# while True:
# minn, maxx = 1, 100
#     n = random.randrange(maxx) + minn   # 0~maxx 중에 랜덤으로 나오니까 +1
# print('수를 결정하였습니다. 맞춰보세요.')
# while True:
#     print(minn + "-" + maxx)
#     s = input('>>')
#     break
# =================================================================================================================
import random

tryNum, min1, max1 = 1, 1, 100          # tryNum : 시도횟수
answer = random.randrange(1, 100)
guess = int(input("수를 결정하였습니다. 맞추어 보세요"))
print("1-100")
print("{}>>{}".format(tryNum, guess))
while True:
    if guess == answer:
        print("맞았습니다.")
        moreQ = input("다시 하시겠습니까?(y/n)")
        if moreQ == 'n':
            break
        elif moreQ == 'y':
            guess = int(input("수를 결정하였습니다. 맞추어 보세요"))
            print("1-100")
            tryNum, min1, max1 = 1, 1, 100
    elif guess != answer:
        if guess < answer:
            print("더 높게")
            min1, max1 = guess, max1
            print("{}-{}".format(min1, max1))
            tryNum += 1
            print("{}>>".format(tryNum), end='')
            guess = int(input())
        else:
            print("더 낮게")
            min1, max1 = min1, guess
            print("{}-{}".format(min1, max1))
            tryNum += 1
            print("{}>>".format(tryNum), end='')
            guess = int(input())
