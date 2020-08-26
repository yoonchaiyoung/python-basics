#

# 변수 이름은 문자, 숫자, _로 구성된다.
friend = 1
a = 10
my_name = '윤채영'
_yourName = '둘리'


print(friend, a)

# 에러
# 특수문자는 _만 가능
# friend$ = 1
# a! = 2
# 숫자는 앞에 오면 안됨
# 1abc = 10
# keyword(예약어)는 변수 이름으로 사용할 수 없음
# def

import keyword
print(keyword.kwlist)

# 한글이름 변수 사용하기
가격1 = 2000
print(가격1)


