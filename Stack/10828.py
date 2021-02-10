# 스택
import sys
stack = []

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    command = sys.stdin.readline().rstrip()

    if " " in command:  # 입력 문자열 : 공백이 포함된건 push
        c, number = command.split()
        stack.append(int(number))
    elif command == 'pop':
        if len(stack) > 0:
            print(stack.pop(-1))
        else:
            print(-1)

    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        print(1 if len(stack) == 0 else 0)
    elif command == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
