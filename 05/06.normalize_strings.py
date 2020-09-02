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
# data ============> data0 ===> data2 ===> data3 ===> data4 ===> insight
#       crawling           p_f2      p_f3        a_f1       a_f2
def clean_strings(strings, *funcs):          # 처리하고 싶은 함수를 튜플로 줘라. 그러면 수정 안해줘도 됨.
                                            # 함수의 갯수가 정해져있지 않음
    results = []
    for s in strings:
        for f in funcs:
            s = f(s)
        results.append(s)
    return results






states = clean_strings(states, str.strip, lambda x: re.sub('[?!#*&$@]', '', x), str.title)
print(states)

