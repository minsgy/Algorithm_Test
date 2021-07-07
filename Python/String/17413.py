# 단어 뒤집기 2
import sys

s = list(sys.stdin.readline().rstrip().split())

for i in range(len(s)):
    if '<' and '>' in s[i]:
        continue
    else:
        s[i] = s[i][::-1]
print(s)
