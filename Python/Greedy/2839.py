# 설탕도둑
# BOJ 2839

# 주문한 설탕 값
number = int(input())
# 봉지 개수
count = 0

max_length = number // 5  # 5개 봉지 경우의 수 파악함.

for i in reversed(range(max_length+1)):  # 5개 봉지 경우의 수 파악.
    count = 0
    copy_number = number  # 반복해야하니 반복마다 저장
    count = i  # 5개 봉지 개수 세기
    i *= 5  # 5개 봉지 설탕 크기 계산
    copy_number -= i  # 5개 봉지 크기 값 뺀 상황.
    if copy_number > 0:  # 남은 설탕이 있을 시, 3개 반복 경우를 살펴본다.
        count += copy_number // 3
        copy_number %= 3

    if copy_number == 0:  # 설탕 크기가 0이 될 시, 그대로 종료
        print(count)  # 봉지 개수 출력
        exit()  # 강제 종료

# 반복문 탈출 시, 남은 설탕이 있으므로 -1 출력함.
print(-1)
