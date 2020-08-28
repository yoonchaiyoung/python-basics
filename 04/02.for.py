# for ~반복문
# for o in (sequence 객체) :

print('\n---------------------------')

for number in [10, 20, 30, 40]:
    print(number)

for number in [10, 20, 30, 40]:
    result = number**2
    print(result, end=' ')
else:
    print('') # print('', end='\n')과 동일함 # 한줄 뛰기 위해서 만듦


print('\n---------------------------')

a = ['cat', 'cow', 'tiger']
for animal in a:
    print(animal, end=' ')
else:
    print('')

print('\n---------------------------')

# 복합자료
# 리스트 안에 튜플이 들어가있는 것
# 복합 자료형을 for문에서 사용하는 경우
l = [('둘리', 10), ('마이콜', 30), ('또치', 11)]
for t in l:
    print(t)

for t in l:
    print('이름: %s, 나이:%d' % t) # t[0], t[1] 하는 거 아님

print('\n---------------------------')

# 10번 반복하는 Loop
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(i)

for i in range(0, 10):
    print(i, end=' ')
else:
    print('')

print('\n---------------------------')

# 1 ~ 10 합을 구하기
sum = 0
for i in range(1, 10+1):
    sum += i
print(sum)

# break
for n in range(10):
    if n > 5:
        break
    print(n, end=' ')
else: # 끝까지 9까지 가야지 else까지 옴
    print('\n-------------')


for n in range(10):
    if n == 5:
        break
    print(n, end=' ')
else: # 끝까지 9까지 가야지 else까지 옴
    print('\n-------------')

print('\n-------------')
for n in range(10):
    if n > 5:
        continue        # 5까지는 출력하고 6부터는 출력안됨
    print(n, end=' ')
else: # 끝까지 9까지 가야지 else까지 옴
    print('\n-------------')

print('\n----------------')
for n in range(10):
    if n <= 5:
        continue        # 이건 0부터 5까지는 출력이 안되고, 6부터 9까지 출력이 됨
    print(n, end=' ')
else :
    print('\n----------')

# continue : 위로 올라가버림. 밑에걸 실행 안 시켜버림.



for i in range(1, 10):
    for j in range(1, 10):
        print("%d X %d = %d" % (i, j, i*j))
    print("-------------------")



# 구구단
print('\n------구구단1------------')
for i in range(1, 10):
    for j in range(1, 10):
        print("%d X %d = %d" % (i, j, i*j))

print('\n--------구구단2------')
for i in range(1, 10):
    for j in range(1, 10):
        print("{0} X {1} = {2}".format(j, i, j*i), end='\t')
    else:
        print('')


print('\n---------삼각형--------')
for i in range(10):
    for j in range(0,i):
        print('*', end='')
    else:
        print('')

print('\n--------삼각형2----------')
for i in range(10):
    print('*' * (i+1))



print('\n-------역삼각형2------')
for i in range(10,0,-1):
    print('*' * i)


