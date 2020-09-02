# 문자열 데이터를 분석전처리 함수 만들기

# 1. 공백제거
# 2. 필요 없는 문자 부호 제거
# 3. 대소문자 정리(Capitalize)

# 4. '--' + string + '--'
# 새로 추가. 확장. (수정X)

import re

states = ['Alabama', 'Georgia!', 'Georgia ', 'georgia', 'FlOrIda', 'south carolina ', 'West virginia?']


def clean_string(strings):
    results = []
    for string in strings:
        # 처리 1
        string = string.strip()
        # 처리 2
        string = re.sub('[?!#*&$@]', '', string)
        # 처리 3
        string = string.title()
        results.append(string)
    return results


states = clean_string(states)
print(states)



##############################################################################################################


states = ['Alabama', 'Georgia!', 'Georgia ', 'georgia', 'FlOrIda', 'south carolina ', 'West virginia?']
# data ===> data1 ===> data2 ===> data3
#       f1         f2         f3
def clean_string(strings, *funcs):          # 처리하고 싶은 함수를 튜플로 줘라. 그러면 수정 안해줘도 됨.
                                            # 함수의 갯수가 정해져있지 않음
    results = []
    for s in strings:
        for f in funcs:
            s = f(s)
        results.append(s)
    return results



# def f1(a):
#     r = str.strip(a)
#     return r

# clean_string(states, f1)


# def strip(a):
#     r = str.strip(a)
#     return r
# 굳이 필요 없음.

def remove_special(a):
    return re.sub('[?!#*&$@]', '', a)


clean_string(states, str.strip, remove_special)
print(states)


















