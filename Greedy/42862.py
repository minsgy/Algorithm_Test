def solution(n: int, lost: list, reserve: list) -> int:
    answer = 0 # 수업 가능 인원
    overlap_list = list(set(reserve) & set(lost)) 
    # lost와 reserve의 중복 값을 저장하는 리스트, 여벌과 잃어버린 리스트에 동시 존재하기 때문에
    
    for item in overlap_list: # 중복 된 값을 리스트에서 다 삭제한다.
        lost.remove(item)
        reserve.remove(item)
        
    answer = n - len(lost); # 전체 인원 - 체육복이 없는 인원 = 체육을 할 수 있는 인원
    for item in lost:
        if (item - 1) in reserve: # 앞에 체육복 남는 인원
            answer += 1 # 체육 가능 인원 증가
            reserve.remove(item-1) # 체육복을 빌려줬으니, 여벌 인원 리스트에서 삭제
        elif (item + 1) in reserve: # 뒤에 체육복 남는 인원
            answer += 1 # 체육 가능 인원 증가
            reserve.remove(item+1) # 체육복을 빌려줬으니, 여벌 인원 리스트에서 삭제
        else: # 없을 경우 다음 잃어버린 학생
            continue
            
    return answer
    
solution(5, [2,4], [1,3,5])