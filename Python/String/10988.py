# 팰린드롬인지 확인하기
import sys
word = sys.stdin.readline().rstrip()

word_reversed = ''.join(list(reversed(word)))
if word == word_reversed:
    print(1)
else:
    print(0)
