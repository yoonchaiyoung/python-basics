# zip() 사용 예
# 여러 순차형을 하나로 묶어준다.

seq1 = {'foo', 'bar', 'baz'}
seq2 = {'one', 'two', 'three', 'four'}

z = zip(seq1, seq2)
print(z, type(z))
# seq2의 'four'는 짝이 맞지 않아 무시.

for t in z:
    print(t)
# 순회를 한 번 하고나면 되돌릴 수 없음.
# sequence 는 for문을 한번 돌고나면 돌릴 수 없음.

# zip 객체 : 한번 순회하면 내용이 비어버림.
# 제너레이터이므로 실제 내부 데이터는 담고 있지 않음.
z = zip(seq1, seq2)
for index, t in enumerate(z):
    print(index, t)
print(list(z))  # 출력값 : []  # 비어있음.

z = zip(seq1, seq2)
for a, b in z:
    print(a, b)
