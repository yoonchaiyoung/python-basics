# zip() 사용 예

seq1 = {'foo', 'bar', 'baz'}
seq2 = {'one', 'two', 'three'}

z = zip(seq1, seq2)
print(z, type(z))

for t in z:
    print(t)
# 순회를 한 번 하고나면 되돌릴 수 없음.
# sequence 는 for문을 한번 돌고나면 돌릴 수 없음.

z = zip(seq1, seq2)
for index, t in enumerate(z):
    print(index, t)

z = zip(seq1, seq2)
for a, b in z:
    print(a, b)
