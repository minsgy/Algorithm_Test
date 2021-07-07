# 좋은 단어
import sys
number = int(sys.stdin.readline().rstrip())
count = 0

for _ in range(number):
    stack = []
    word = sys.stdin.readline().rstrip()
    for i in word:
        if not stack or i != stack[-1]:
            stack.append(i)
        else:
            stack.pop()

    if not stack:
        count += 1

print(count)
