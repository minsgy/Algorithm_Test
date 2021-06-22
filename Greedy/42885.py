def solution(people: list, limit: int) -> int:
    answer = 0
    people.sort()
    
    left = 0
    right = len(people) - 1
    
    while left < right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        answer += 1
    
    if left == right: 
    # Testcase 2 - 값이 다 더해지지 않을 시, left=right 같아짐.
        answer += 1
    
    return answer


solution([70, 50, 80, 50], 100)