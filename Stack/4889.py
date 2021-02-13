import sys
# 안정적인 문자열
while True:
    stack = []
    i = 1
    count = 0
    word = sys.stdin.readline().rstrip()

    if '-' in word:
        exit()

    for n in word:
        if n == '{':
            stack.append(n)
        else:
            if stack:
                stack.pop()
            else:
                count += 1
                stack.append("{")

    if stack:
        count += len(stack) // 2

    print(str(i)+'. '+str(count))
    i += 1
