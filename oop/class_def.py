# 클래스 정의 테스트
# 가장 최상위 클래스는 object
class MyString:
    pass

print("==== MyString Class")
s = MyString()  # 인스턴스화
print(type(s))

print("s의 클래스 확인:", s.__class__)    # 출력값 : <class '__main__.MyString'>
print("MyString의 부모 확인:", MyString.__bases__)   # 출력값 : (<class 'object'>,)
# 파이썬은 여러 부모로부터 상속을 받을 수 있다.

print("s의 구성 요소:", dir(s))
print("object의 구성 요소:", dir(object))