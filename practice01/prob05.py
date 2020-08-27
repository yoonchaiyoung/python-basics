# 문제5.
# 주어진 리스트 데이터를 이용하여 3의 배수의 개수와 배수의 합을 구하여 출력형태와 같이 출력하세요.

l = [10, 12, 14, 15, 17, 18, 19, 20, 25, 30, 32, 33, 37, 40, 42, 44, 46, 50]

multiple3count = 0
multiple3sum = 0
for number in l:
    if number % 3 == 0:
        multiple3count += 1
        multiple3sum += number

print('주어진 리스트에서 3의 배수의 개수=>', multiple3count)
print('주어진 리스트에서 3의 배수의 합=>', multiple3sum)

