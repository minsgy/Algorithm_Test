# 프로그래머스 SUMMER/WINTER CODING 소수만들기
from itertools import combinations
def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임


def solution(nums: list) -> int:
    CList = list(combinations(nums, 3)) # 조합 구하기    
    answer = 0 # 아무것도 없을 시 0 반환
    for items in CList:
        # 소수 판별 함수를 통해, 합한 값 count 세기
        if is_prime_number(sum(items)):
            answer += 1
    
    return answer