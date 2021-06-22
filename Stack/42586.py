def solution(progresses: list, speeds: list) -> list:
    answer = []
    count = 0
    top = len(progresses) - 1
    
    # stack 처럼 사용하기 위해서.. 
    speeds.reverse()
    progresses.reverse()
    
    while progresses:
        if progresses[top] >= 100:
            count += 1
            top -= 1
            progresses.pop()
        elif count > 0:
            answer.append(count)
            count = 0
        else: 
            for i in range(top+1):
                progresses[i] += speeds[i]
                
    answer.append(count)
    return answer

solution([93, 30, 55], [1, 30, 5], [2, 1])