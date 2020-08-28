# 생성
l1 = []
l2 = [1, True, 'python', 3.14]

print('=============== sequence 타입 특징 ============')

# 인덱싱(sequence 타입 특징)
print(l2[0], l2[1], l2[2], l2[3])
print(l2[-4], l2[-3], l2[-2], l2[-1])

# slicing(sequence 타입 특징)
print(l2[1:4])
# l3 = l2
# l4 = l2[:]
# print(l3 is l2)
# print(l4 is l2)

print(l2[:])
print(l2[2:])
print(l2[3:0:-1])
print(l2[3::-1]) # 역으로 가져오고 싶음
print(l2[len(l2)::-1]) # 길이가 굉장히 길고 길이를 모를 때 len 함수 사용


# 반복(sequence 타입 특징)
l3 = l2 * 2
print(l3)


# 연결(sequence 타입 특징)
l4 = l2 + [1,2,3]
print(l4)

# 길이(sequence 타입 특징)
print(len(l4))

# in, not in(sequence 타입 특징)
print(5 not in l4)
print('python' in l4)


print('=============== 변경 가능한 객체 ============')

# 삭제(변경 가능한 객체)
del l4[2]
print(l4)

# 변경 가능한 객체(mutable)
l5 = ['apple', 'banana', 10, 20]
print(l5)
l5[2] = l5[2] + 90
print(l5)


print('=============== slicing 기법 ============')

# 삭제(slicing을 이용한...)
l6 = [1, 12, 123, 1234]
l6[1:3] = [] # 오른쪽걸로 대신 대입. 치환..
print(l6)

l6[0:] = []
print(l6)

# 삽입(slicing을 이용한...)
l7 = [1, 123, 1234, 12345]

# 처음 삽입
l7[:0] = [-129, -12, -1, 0]
print(l7)

# 중간 삽입
l7[1:1] = [123]
# l7[1:2] 이렇게 해버리는 치환이 되버림
print(l7)

# 마지막 삽입
l7[5:5] = [123456]
print(l7)


# 치환(slicing을 이용한...)
l8 = [1, 12, 123, 1234, 12345]
l8[0:2] = [10, 20] # 치환을 하려면 갯수를 맞춰서
print(l8)

l8[0:2] = [100] # 갯수를 맞추지 않으면 2개 지우고 1개만 만들어서 전체 갯수가 4개가 됨.
print(l8)

l8[1:2] = [200]
print(l8)

l8[2:4] = [300, 400, 500, 600]
print(l8)


print('=============== 객체함수 ============')
l9 = [1, 3, 4]

# 처음 삽입
l9.insert(0,0)
print(l9)

# 중간삽입
l9.insert(1,2)
print(l9)

# 마지막 삽입
l9.append(5)
l9.append([5,6])
print(l9)


# reverse
l9.reverse()
print(l9)

# 삭제(값으로 삭제, 동질한 객체를 삭제한다. ==를 이용)
l9.remove(3) # index가 아니라 지울 것을 입력
print(l9)

# 없는 객체 삭제할 경우
# l9.remove(3)
# print(l9)
# # 출력결과 : Process finished with exit code 1

try:
    l9.remove(3)
except ValueError as e:
    print('없는 객체 삭제할 경우 예외 발생')


# 확장
l9.extend([-1, -2, -3])
print(l9)

# stack
s = []
s.append(10)      # push
s.append(20)      # push
s.append(30)      # push

print(s)

print(s)                  # 출력결과 : [10, 20, 30]
print(s.pop())    # pop   # 출력결과 : 30
print(s.pop())    # pop   # 출력결과 : 20
print(s)                  # 출력결과 : [10]

# queue로 사용해보기
q = [1, 2]
q.append(3)
q.append(4)
q.append(5)

print(q)                 # 출력결과 : [1, 2, 3, 4, 5]
print(q.pop(0))          # 출력결과 : 1
print(q.pop(0))          # 출력결과 : 2
print(q.pop(0))          # 출력결과 : 3

print(q)                 # 출력결과 : [4, 5]


# sort
l10 = [1, 5, 3, 9, 8, 11]
l10.sort()                      # l10.sort(key=int) 과 동일
print(l10)
# 오름차순 정렬

l11 = [10, 2, 33, 9, 8, 4, 11]
l11.sort(key=str)               # string으로 보면서 정렬
                                # 즉, l11 = ['10', '2', '33', '9', '8', '4', '11']
                                # 이렇게 보겠다.
                                # '10' 은 맨 앞이 1로 시작. '2'는 맨 앞이 2로 시작.
                                # '10'이 '2'보다 앞 순서다.

                                # 즉, l11.sort(key=str()) 이거임.
print(l11)


# cf: sorted 전역함수

l12 = [19, 46, 37, 28, 91, 55, 64]
l13 = sorted(l12)
print(l12)

# sorted 안에 알고리즘, 함수 같은 거 넣을 수 있음.
# 객체함수는 자기 자신을 바꾸지만
# 전역함수는 자기 자신을 바꾸지 않는다.


def f(i):
    return i % 10

l14 = sorted(l12, key=f, reverse=False)         # sorted 안에 함수를 넣음
                                                # 10으로 나눈 나머지니까 일의 자리
                                                # 일의 자리를 기준으로 배열
print(l14)

