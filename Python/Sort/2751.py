def solution(n: int) -> list:
    a = []
    for i in range(n):
        a.append(int(input()))

    a.sort()
    
    for j in a:
        print(j)    

n = int(input())
solution(n)
