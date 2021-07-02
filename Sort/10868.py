import sys
def solution(n, k):
  lists = []
  answer = []
  for _ in range(n):
    temp = sys.stdin.readline().rstrip()
    lists.append(int(temp))
  
  for _ in range(k):
    x, y = map(int, input().split())
    answer.append(min(lists[x-1:y]))
    
  for item in answer:
    print(item)

n, k = map(int, input().split())
solution(n, k)