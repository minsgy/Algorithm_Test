# 괄호의값

import sys

n = sys.stdin.readline().rstrip()

stack = list()

for i in n:
    # 닫힌 태그 발견 시, 옳은 계산인지 확인하고, 옳다면 안에 든 스택을 다삭제하면서 숫자 값 계산을 저장한다.
    if i == ")":
        temp = 0

        while stack:
            top = stack.pop()
            if top == "(":
                if temp == 0:
                    stack.append(2)
                else:
                    stack.append(2 * temp)
                break
            elif top == "[":
                print("0")
                exit(0)
            else:
                if temp == 0:
                    temp = int(top)
                else:
                    temp = temp + int(top)

    elif i == "]":
        temp = 0

        while stack:
            top = stack.pop()
            if top == "[":
                if temp == 0:
                    stack.append(3)
                else:
                    stack.append(3 * temp)
                break
            elif top == "(":
                print("0")
                exit(0)
            else:
                if temp == 0:
                    temp = int(top)
                else:
                    temp = temp + int(top)
    # 숫자는 계속해서 스택에 추가한다. (닫힌 태그 일때만 계산하기 때문이다.)
    else:
        stack.append(i)

result = 0

for i in stack:
    if i == "(" or i == "[":
        print(0)
        exit(0)
    else:
        result += i

print(result)
