# 나이순 정렬
import sys

n = int(sys.stdin.readline().rstrip())

dic = {}
for _ in range(n):
    age, name = sys.stdin.readline().rstrip().split()
    dic[name] = int(age)

dic = sorted(dic.items(), key=lambda x: x, reverse=True)

for name, age in dic:
    print(str(age) + ' ' + name)
