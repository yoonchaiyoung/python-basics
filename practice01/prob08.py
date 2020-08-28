# 문제8.
# 문자열을 입력 받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요.
#
# <<실행결과>>
# 입력>  Python Programming!
# 결과> !gnimmargorP nohtyP

# 교수님
# def reverse(s):
#     results = ''
#     return results
#
# s = input('입력>')
# reverse(s)
# print('결과'>{0}.format(s))
#
# # reverse 함수 사용하지 말고 직접 알고리즘 짜보기.

# =================================================================================================================

string = input("입력>")
list1 = []

def reverse(s):
    for i in range(len(string)-1, 0-1, -1):
        list1.append(string[i])
    ans = ''.join(list1)
    return ans
print("결과>", reverse(string))