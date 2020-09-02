import sys

print('========= 가변인수 ==========')
print(1)
print('hello', ' ', 'world')

print('========= sep 기본 인수값 ==========')
x = 0.2
s = 'hello'
print(str(x) + ' ' + s)

print(x, s)

print(x, s, sep=' ')
print(x, s, sep=':')


print('========= end 기본 인수값 ==========')
print('hello world')
print('!!!!!!!!!!!!!!!!')
print('hello world', end='\n')
print('!!!!!!!!!!!!!!!!')
print('hello world', end='')
print('!!!!!!!!!!!!!!!!')


print('========= file 기본 인수값 ==========')
# print('hello world', file=sys.stdout)
print('hello world')
print('error: hello world', file=sys.stderr)
# 맨 앞줄에 출력

f = open('hello.txt', 'w')              # write 모듈
print(type(f))
print('hello world', file=f)
f.close()                               # 내가 연거는 반드시 닫아야 함

# 06 이라는 디렉토리에 hello.txt 파일을 만들음
# 파일을 추상화시켰다고 보면 됨.


# 참고
sys.stdout.write('hello world!!!!!!!!!!!!!!!!!!!!')
