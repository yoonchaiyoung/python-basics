# 문제4.
# 다음과 같은 출력이 되도록 구구단을 작성하세요. (이중 for~in)
# 1 x 1 = 1   2 x 1 = 2   3 x 1 = 3   ... 9 x 1 = 9
# 1 x 2 = 2   2 x 2 = 4 ...
# ...
# 1 x 9 = 9   2 x 9 = 18 ...

for i in range(1,9+1):
    for j in range(1,9+1):
        print("%d x %d = %d" % (j, i, i*j), end='\t')
    print('')