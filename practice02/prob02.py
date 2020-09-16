# 문제2. 다음과 같은 텍스트에서 모든 태그를 제외한 텍스트만 출력하세요.
#
# s = """
# <html>
#     <body style='background-color:#ffff'>
#         <h4>Click</h4>
#         <a href='http://www.python.org'>Here</a>
#         <p>
#         	To connect to the most powerful tools in the world.
#         </p>
#     </body>
# </html>"""


# =================================================================================================================

s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
            To connect to the most powerful tools in the world.
        </p>
    </body>
</html>"""

list1 = []
for i in range(len(s)):
    list1.append(s[i])
print(list1)
# s 를 한글자씩 빼내서 리스트로 만들었다.

indexList = []
for i in range(len(list1)):
    if list1[i] in ['<', '>']:
        indexList.append(i)
print(indexList)
# 태그의 <, > 괄호의 위치(index)를 담은 리스트를 만들었다.


for j in range(int(1/2 * len(indexList))):
    # print(indexList[2*j], indexList[2*j +1])    # < 위치, > 위치
    list1[indexList[2*j] : indexList[2*j +1] +1] = ' ' * len(list1[indexList[2*j] : indexList[2*j +1] +1])
# <태그내용> 을 전부 ' ' 공백으로 바꿨다.


results = ''        # 결과를 출력할 문자열
for k in range(len(list1)):
    print(list1[k], end='')
