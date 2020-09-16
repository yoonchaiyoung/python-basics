# 문제3.
#
# 1)다음 문자열을 모든 소문자를 대문자로 변환하고, 문자 ',', '.','\n'를 없앤 후에 중복
# 없이 각 단어를 순서대로 출력하세요.
# s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
# in this guide, then the Python Mentors group is available to help guide new contributors through the process."""
#
# 실행 결과:
# AFTER
# AVAILABLE
# CONTRIBUTE
# CONTRIBUTORS
# .
# .
# .
# .
# .
# TO
# WE
# YOU
#
# 2)각 단어의 빈도수도 함께 출력해 보세요
# 실행 결과:
# AFTER:1
# AVAILABLE:1
# CONTRIBUTE:1
# CONTRIBUTORS:1
# ENCOURAGE:1
# EVERYONE:1
# GROUP:1
# GUIDE:2
# HAVE:1
# HELP:1
# IF:1
# IN:2
# IS:2
# .
# .
# .
# .
# .
# .
# THROUGH:1
# TO:5
# WE:1
# YOU:1



# (교수님 힌트)
# split
# ' '
# 중복없이 => set으로 바꾸기
# =================================================================================================================

# 1)
s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""
s1 = s.upper()
s1 = s1.replace(",", "")
s1 = s1.replace(".", "")
s1 = s1.replace("\n", "")
s1 = s1.split(" ")          # s1 : 단어 전부 다 담아놓은 리스트
s2 = set(s1)
s2 = list(s2)
s2 = sorted(s2)             # s2 : 단어 중복없이 담아놓은 리스트
for word in s2:
    print(word)


# 2)
# s1의 단어들 하나씩 빼서 중복없는 리스트와 비교
# 있을 때마다 갯수 +1
count_list = [0] * len(s2)
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            count_list[j] += 1
for z in range(len(count_list)):
    print("{}:{}".format(s2[z],count_list[z]))
