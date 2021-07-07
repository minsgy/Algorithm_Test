# 프로그래머스 완전탐색 - 모의고사
# 1번 - 1,2,3,4,5
# 2번 - 2,1,2,3,2,4,2,5
# 3번 수포자 - 3,3,1,1,2,2,4,4,5,5 
# 반복 규칙을 규정해보자 
def solution(answers):
    answer = []
    count = [0]*3
    
    number_1 = [1,2,3,4,5]
    number_2 = [2,1,2,3,2,4,2,5]
    number_3 = [3,3,1,1,2,2,4,4,5,5]

    for i in range(len(answers)):
        number_1st_len = i % 5
        number_2nd_len = i % 8
        number_3rd_len = i % 10
        
        if number_1[number_1st_len] == answers[i]:
            count[0] += 1
        if number_2[number_2nd_len] == answers[i]:
            count[1] += 1
        if number_3[number_3rd_len] == answers[i]:
            count[2] += 1

    # 고득점자 빼기
    max_index = max(count)
    # 고득점에 해당되는 수포자 뽑기
    for i in range(len(count)):
        if max_index == count[i]:
            answer.append(i+1)

    return answer

answers = [1,2,3,4,5]
solution(answers)