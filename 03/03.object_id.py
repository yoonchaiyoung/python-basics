# id 함수 : 실제 객체의 주소를 반환
i1 = 10
i2 = 20

print(id(i1), id(i2))
# 주소 뜸

print(hex(id(i1)), hex(id(i2)))
# 16진수?로 바꿔봄
# 두개 주소가 다름

i1 = 1234567890
i2 = 1234567890

print(hex(id(i1)), hex(id(i2)))
# 두개 주소 동일함

i1 = 11
i2 = 10 + 1
print(hex(id(i1)), hex(id(i2)))

# 가변 객체
l1 = [1,2,3]
l2 = [1,2,3]
print(hex(id(l1)), hex(id(l2)))
# 두 개의 주소 다름

s1 = 'hello'
s2 = 'hello'
print(hex(id(s1)), hex(id(s2)))

# is (동일 레퍼런스 비교)
# 가변 객체는 is(동일성)과 ==(동질성)의 결과 다름 (list, set, dict)
# 불변 객체는 is(동일성)과 ==(동질성)의 결과 같음 (나머지)

print(i1 is i2)
# 출력값 : True    이유 : 불변 객체
print(l1 is l2)
# 출력값 : False    이유 : 가변 객체(리스트)
print(s1 is s2)
# 출력값 : True    이유 : 불변 객체


# ?
t1 = (1, 2, 3)
t2 = (1, 2, 3)
print(t1 is t2)
# 출력값 : True     이유 : 불변 객체(튜플)



if i2 - 10 == True:
    pass
# 이렇게 하는 것보다

if i2 - 10 is True:
    pass
# 이게 더 좋음

# 동일성 비교를 해주는 것이 좋음.


# 형변환 함수는 불변 객체라고 하더라도 새로운 객체를 만든다.
# (바로 대입하는 = 과는 다르게 작동한다.)

# range(1, 4) # 얘는 가변객체
r = range(1, 4)
print(r, type(r))
# 출력결과 : range(1, 4) <class 'range'>
t3 = tuple(range(1, 4))
print(t3)
print(t1 is t3)
# 출력결과 : False

# 내용은 같지만 다른 객체



# slicing 경우에는...
t4 = (0, 1, 2, 3)[1:]
print(t1 is t4)
#출력결과 : False




