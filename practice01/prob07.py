# 문제 7.
# 키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오
#
# <<실행결과>>
# > 1
# > 2
# > 3
# > 4
# > 5
# 평균: 3.0

# =================================================================================================================


numberList = []
numberList.append(int(input("정수를 입력해주시고 엔터키를 눌러주세요: ")))
numberList.append(int(input("정수를 입력해주시고 엔터키를 눌러주세요: ")))
numberList.append(int(input("정수를 입력해주시고 엔터키를 눌러주세요: ")))
numberList.append(int(input("정수를 입력해주시고 엔터키를 눌러주세요: ")))
numberList.append(int(input("정수를 입력해주시고 엔터키를 눌러주세요: ")))

sum0 = 0
for i in numberList:
    sum0 += i
avg0 = sum0 / len(numberList)
print("평균:",avg0)