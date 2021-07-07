import sys
from collections import defaultdict

def solution(n):
  dic = defaultdict(int)
  for _ in range(n):
    number = int(sys.stdin.readline())
    dic[number] += 1
  
  dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
  print(dic[0][0])

n = int(input())
solution(n)  