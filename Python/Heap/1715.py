# 백준 - 카드 정렬하기
import heapq
import sys
def solution(n: int) -> int:
  card_list = []
  answer = 0
  for _ in range(n):
    card_list.append(int(sys.stdin.readline().rstrip()))
    
  heapq.heapify(card_list)
  
  while len(card_list) >= 2:
    a = heapq.heappop(card_list)
    b = heapq.heappop(card_list)
    result = a + b
    answer += result 
    heapq.heappush(card_list, result)
  
  print(answer)

n = int(input())
solution(n)