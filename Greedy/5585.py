# 거스름돈
def algorithm(money):
    money_list = [500, 100, 50, 10, 5, 1]
    count = 0
    # 500엔 부터 하나씩 비교해서 카운트 증가시키기
    for n in money_list:
        count += money // n  # 카운트 = 동전 개수 쌓기
        money %= n  # 나머지 값 money에 저장

    return count


money = int(input())
# 1000을 냈을 때, 나올 거스름돈을 줘야 하기 때문이다.
print(algorithm(1000-money))
