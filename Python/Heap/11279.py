import heapq

def solution(n):
    answer = []
    result = []
    heapq.heapify(answer)
    for i in range(n):
        result = int(input())
        heapq.heappush(answer, result)
    while answer:
       print(heapq.heappop(answer))
    

n = int(input())
solution(n)