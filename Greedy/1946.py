# 신입 사원
import sys


test_case = int(input())
for _ in range(test_case):
    number = int(sys.stdin.readline())
    result = []
    count = 1  # 합격 최대 인원수, 1인 이유는 기본적으로 1등인 애가 기준이기때문.
    for _ in range(number):
        test1, test2 = map(int, input().split())
        result.append([test1, test2])

    result.sort(key=lambda x: (x[0], x[1]))

    min_cut = result[0][1]  # 기준점
    for rs in result[1:]:
        if min_cut > rs[1]:
            min_cut = rs[1]
            count += 1
    print(count)
