def dummy():
    pass


def my_function():
    print('Hello World')


# 여러개 값을 반환할 수 있다.(사실은 tuple 의 auto packing과 unpacking을 파이썬이 지원을 해준다.)
def my_function2():
    return (10, 20)    # 자동으로 패킹되니까 (10, 20)말고 그냥 10, 20 이라고 써도 됨.


def my_function3(id):
    print('{0}님 안녕하세요'.format(id))


def my_function4(a,b):
    return a * b


def none():
    print('some codes...1')
    if 10 - 9 is 1:
        return
    print('some codes...2')

# 함수는 객체다. (함수를 값처럼 다룰 수 있다.)
# 함수 자체를 parameter로 넘길 수 있다는 이야기
def my_function5(f):
    f()




dummy()
my_function()

# t = my_function2()
# print(t)

i, j = my_function2()
print(i, j)
my_function3('kickscar')

r = my_function4(10, 20)
print(r)

none()

my_function5(my_function)
print(my_function, type(my_function))

