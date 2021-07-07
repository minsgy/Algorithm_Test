def solution(numbers: list) -> str:
    lists = []
    answer = ""
    for i in numbers:
        lists.append([str(i),str(i)*3])
    lists.sort(reverse=True, key=lambda x: x[1])
    for item in lists:
        answer += item[0]

    return str(int(answer))

solution([6, 10, 2])
solution([3, 30, 34, 5, 9])