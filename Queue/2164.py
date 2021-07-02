from collections import deque
def solution(n):
  queue = deque([k for k in range(1, n+1)])
  while len(queue) > 1 :
    queue.popleft()
    temp = queue.popleft()
    queue.append(temp)
  
  print(queue[0])

n = int(input())
solution(n)