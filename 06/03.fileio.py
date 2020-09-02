
# text mode가 default " t(생략가능)
f = open('test_t.txt', 'wt', encoding='utf-8')
w_sz = f.write('안녕하세요.\n파이썬입니다.')
f.close()
print(w_sz)                 # 14개 문자를 적음.

# binary mode : b
f = open('test_b.txt', 'wb')
w_sz = f.write(bytes('안녕하세요.\n파이썬입니다.', 'utf-8'))
f.close()
print(w_sz)

# read test
f = open('test_t.txt', 'rt', encoding='utf-8')
text = f.read()
f.close()
print(text)

# read test : binary mode -> copy.py
