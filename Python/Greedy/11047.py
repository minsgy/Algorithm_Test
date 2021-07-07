# 동전 0

def algorithm(n, k):
    result = []
    count = 0
    for _ in range(n):
        temp = int(input())
        result.append(temp)  # 동전 종류 삽입.

    for n in result[::-1]:
        if n <= k:
            count += k // n
            k %= n

    return count


# 동전 종류 개수 n, 가진 돈 k
n, k = map(int, input().split())
print(algorithm(n, k))
