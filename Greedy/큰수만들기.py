import sys


def solution(number, k):
    answer = []  # 결과 담을 리스트
    count = 0  # 하나하나 증가하면서 탐색하기 때문에.
    result_length = len(number) - k  # 결과 10 - 4 = 6
    for i in range(0, len(number)):
        max = "0"
        for j in range(count, len(number)):
            if number[i] > max:
                max = number[i]
                count = i
                if number[i] == "9":
                    break
        if max == "0":
            count = 0
        answer.append(max)

    return answer


solution("4177252841", 4)
