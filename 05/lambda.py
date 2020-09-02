def f(x):
    r = x * x
    return r


for i in range(10):
    s = '{0}:{1}'.format(i, f(i))
    print(s)

# 람다로 표현해보자.
# 함수 이름 X

for i in range(10):
    s = '{0}:{1}'.format(i, (lambda x: x * x)(i))
    print(s)


