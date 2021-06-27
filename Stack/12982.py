def solution(d: list, budget: int) -> int:
    # 정렬을 통해서, 리스트 합이 budget 보다 클 시, 큰 값 부터 삭제
    # 남은 list의 길이가 최대 지원 부서 값
    d.sort() # 1, 2, 3, 4, 5
    
    while sum(d) > budget:
        d.pop() # 큰 값 부터 제거
        
    return len(d)