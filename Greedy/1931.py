
# 입력 회의 개수

# 종료 시간이 빠른 순서대로 정렬하자.
# 종료 시간이 같을 경우, 시작 시간이 더 빨라야함.
def algorithm(n):
    count = 1  # 시작하는 회의 개수 값
    time_check = []
    for _ in range(n):
        temp1, temp2 = map(int, input().split())
        time_check.append([temp1, temp2])

    # 종료시간 기준 오름차순으로 정렬한다.
    time_check[1].sort()
    # time : 현재 회의 종료시간 설정
    time = time_check[0][1]
    for i in range(len(time_check)):
        # 현 회의에 끝나는 시간이 뒷 회의 시작 시간보다 작아야함.
        # 그래야 회의가 끝난 상태에서 회의가 가능하기 때문이다.
        if time < time_check[i][0]:
            # 회의가 끝난 상태에서의 들어온 회의
            count += 1  # 가능한 회의 개수 증가
            time = time_check[i][1]  # 현재 진행 중인 회의 시간 재설정

    return count  # 실행 회의 개수 반환


n = int(input())
print(algorithm(n))
