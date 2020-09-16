# 문제 5. 선택정렬(제자리 정렬 알고리즘)을 적용하는 코드를 완성하세요.
# 문제에 주어진 배열 [ 5, 9, 3, 8, 60, 20, 1 ] 를 크기 순서대로 정렬하여 다음과 같은 출력이 되도록 완성하는 문제입니다.
#
# nums = [5, 9, 3, 8, 60, 20, 1]
#
# print('Before Sort.')
# for num in nums:
#     print(num, end=' ')
# else:
#     print()
#
# count = len(nums)
#
# #
# # 코드 작성
# #
#
# print("After Sort.")
# for num in nums:
#     print(num, end=' ')
# else:
#     print()
#
# =================================================================================================================

list1 = [5, 9, 3, 8, 60, 20, 1]
list2 = []
for i in range(len(list1)):
    for j in range(-len(list1)+1, 0, 1):
        if list1[0] > list1[j]:
            list1[0], list1[j] = list1[j], list1[0]
    list2.append(list1[0])
    del list1[0]
print(list2)
