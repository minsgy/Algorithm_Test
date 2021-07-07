import sys
# 전화번호 목록
T = int(sys.stdin.readline())
for _ in range(T):

    li = []
    flag = 0

    n = int(sys.stdin.readline())
    for _ in range(n):
        li.append(sys.stdin.readline().strip())

    li.sort()
    flag = 0

    for i in range(len(li)-1):
        # 인자값이 앞 문자열안에 존재하면 True, 없으면 false (튜플만 넣을 수 있음.)
        if li[i+1].startswith(li[i]):
            print("NO")
            flag = 1
            break

    if flag == 0:
        print("YES")
