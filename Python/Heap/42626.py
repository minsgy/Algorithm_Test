# 프로그래머스 - 더 맵게
import heapq
def solution(scoville: list, K: int) -> int:
    answer = 0 # 변환 횟수
    # heap 형태로 변환    
    heapq.heapify(scoville)
    
    # 인덱스 오류 방지를 위해서
    while len(scoville) >= 2:
        min_data = heapq.heappop(scoville) 
        if min_data >= K: # 최소값이 제시 스코빌보다 크거나 같을 시, 전부 확인했기 때문에 반복 정지
            break 
        else:
#             비교 할 두번째 최소 값 반환
            min_data2 = heapq.heappop(scoville)
            result = min_data + (min_data2 * 2)
            heapq.heappush(scoville, result) # 계산한 값 푸시
            answer += 1 # 변환 횟수 숫자 증가
    
    # scoville의 0번째는 최소값이므로, 스코빌 지수 K 확인하기  
    if scoville[0] < K:
        answer = -1
  
    return answer

print(solution([1, 1, 1], 4))