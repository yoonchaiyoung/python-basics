# 생성
d = {'basketball': 5, 'baseball': 9}
print(d, type(d))


d2 = {}
print(d2, type(d2))


d3 = dict()
print(d3, type(d3))


d4 = dict(one=1, two=2, three=3, fout=4)
# key=value
print(d4, type(d4))
# 가변 parameter
# 함수


d5 = dict([('one', 1), ('two', 2), ('three', 3), ('four', 4)])
print(d5, type(d5))
# 리스트를 딕셔너리로 바꿔


# 이 5가지 방법 다 할 줄 알아야 함.
# d 방법이 제일 쉬운데
# 근데 db 에서 리스트로 가져오거나 할 때는 d5 방법처럼 가져올 수도 있잖아


# index 대신에 key로 값(데이터)에 접근한다.
print(d['basketball'])

# print(d[0])
# 에러남. index 없음.
# key, value 있음.

# 크기
print(len(d))

# in, not in : key의 존재 여부만 가능
print('soccer' in d)
print('soccer' not in d)
print('baseball' in d)

# 다양한 타입의 key를 사용할 수 있다.
d6 = {}  # 공딕셔너리
print(d6)

d6['twenty'] = 20    # str
d6[True] = 'True'    # bool
d6[10] = 10
print(d6)
# key는 중복해서 들어가면 안됨.
# key는 변경가능한 리스트가 들어가면 안됨.

# 키는 변경불가능한 타입의 값을 사용해야 한다.
# d6[[1, 2, 3]] = 6
# 에러남..
# 뭐 굳이 하고 싶다면 변경불가능한 애로 바꿔서
d6[(1, 2, 3)] = 6
print(d6)

print("========= 객체함수 =========")
# key 값 출력
k = d6.keys()
print(k, type(k))
# key 값 순회
for key in k:
    print(key, d6[key])
# key value 출력
# 마치 리스트처럼..


# value 값 출력
v = d6.values()
print(v, type(v))
# value 값 순회
for value in v:
    print(value)


items = d6.items()
print(items)
# 출력결과 : dict_items([('twenty', 20), (True, 'True'), (10, 10), ((1, 2, 3), 6)])
# [('twenty', 20), (True, 'True'), (10, 10), ((1, 2, 3), 6)] 이걸 가지고 있는 객체의 이름 : dict_items 라는 의미.
# 클래스..

# items 순회
for item in items:
    print(item)


phones = {'마이콜':'000-0000-0000', '둘리':'111-1111-1111', '또치':'222-2222-2222'}
print(phones['둘리'])
print(phones.get('둘리'))
# get으로 하는 게 더 좋음.

# print(phones['도우넛'])
v = phones.get('도우넛')
if v is None:
    print('도우넛 키를 가진 값은 없습니다.')

# 어떤 로직을 세울 때는 if문으로 하는 것이 좋음.
# 그냥 print(phones.get('도우넛')) 이렇게 하지 말고



v = phones.setdefault('도우넛', '555-5555-5555')
# 만약에 '도우넛'에 해당하는 value 값이 없다면
# None 을 출력하는 것이 아닌
# 555-5555-5555를 출력하고
# 딕셔너리에
# key를 '도우넛', value를 '555-5555-5555'를 추가해라.
print(v)

v = phones.setdefault('둘리', '666-6666-6666')
print(v)
# 둘리는 있으니까 666-6666-6666으로 바뀌지 않고 원래의 값 그대로를 가진다.

print(phones)


# pop() : 삭제와 동시에 값을 가져온다.
v = phones.pop('둘리')
print(v)
print(phones)

# popitem() : 삭제와 동시에 (키, 값) 가져온다.
# 근데 dictionary에는 순서(index)가 없기 때문에 뭘 가져올지는 모른다.
item = phones.popitem()
print(item)
print(phones)
# 도우넛이 빠져서 없어졌다.

# clear()
phones.clear()
print(phones)

# 조회
d7 = {'c':3, 'a':1, 'b':2}

for key in d7:
    print(key, end=' ')
else:
    print('')
# 딕셔너리에서 그냥 for 루프문 사용하면
# key 값 꺼내짐

for key in d7.keys():
    print(key, end=' ')
else:
    print('')
# 동일한 결과 나옴


for key, value in d7.items():
    print(key, value)






