# 사람들 인원수이다.
human = int(input())
# 시간들을 Int형태로 공백을 나누어서 리스트에 삽입한다.
times = list(map(int, input().split()))
# 최소 시간 합
result = 0
# 사람마다의 걸린 시간 저장 리스트
result_list = []

# 필요한 시간의 최솟값을 구하기 위해서는,시간들의 오름차순 정렬로 낮은 시간부터 더해가면 된다.
times.sort()
# 최소값을 제거하면서 값을 더해가는 것도 괜찮을듯?
for i in range(human):
    result += times[i]
    result_list.append(result)
print(sum(result_list))
