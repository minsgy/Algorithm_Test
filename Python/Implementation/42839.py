# 프로그래머스 소수찾기 

import math
from itertools import permutations

def prime_number(n):
    if n == 0 or n == 1:
        return False
    else:
        # 소수는 2부터 숫자의 제곱근까지만 돌려주면 된다.
        sqrt_number = int(n**(1/2))
        for i in range(2, sqrt_number+1):
            if n % i == 0: # 나누어 떨어지면 소수가아니다.
                return False
        return True # 다 돌아도 아니면은 소수
            

def solution(numbers):    
    lists = list(map(int, numbers))
    answer = []
    # 순열을 뽑아서 모든 경우의 수 뽑기
    for i in range(1, len(lists)+1):
        # 공집합은 필요없으니 패스, 본인 글자수만큼 해야하니 +1
        arr = list(permutations(lists, i))
        for j in range(len(arr)):
            num = int(''.join(map(str,arr[j])))
            # 튜플들을 문자열 방식으로 합쳐주고, int형으로 변환
            if prime_number(num):
                answer.append(num)
                
    answer = list(set(answer))
    return len(answer)