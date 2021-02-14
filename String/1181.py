# 단어 정렬
import sys

n = int(sys.stdin.readline().rstrip())
word = []
for _ in range(n):
    temp = sys.stdin.readline().rstrip()
    word.append(temp)

word.sort(key=lambda x: (len(x), x))

lists = []
for i in word:
    if i not in lists:
        lists.append(i)
        print(i)
