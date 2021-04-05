# 단어 수학
import sys

n = int(sys.stdin.readline())
liner = []

words = {}  # 알파벳 저장 딕셔너리 'A': 10000 자리수값을 구한다.
for _ in range(n):
    liner.append(list(sys.stdin.readline().rstrip()))

liner.sort(key=lambda x: len(x), reverse=True)

for i in range(len(liner)):
    for j in range(len(liner[i])):
        if liner[i][j] not in words:
            words[liner[i][j]] = pow(10, len(liner[i])-j-1)
        else:
            words[liner[i][j]] += pow(10, len(liner[i])-j-1)

sort_liner = sorted(words.items(), key=lambda x: x[1], reverse=)
result = 0
num = 9

for i in range(len(sort_liner)):
    result += num * sort_liner[i][1]
    num -= 1


print(result)
