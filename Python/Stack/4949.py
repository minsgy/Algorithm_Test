# 균형잡힌 세상
import sys

while True:
    temp = list(sys.stdin.readline().strip())
    stack = []
    if(temp == '.'):
        break

    for word in temp:
        if word == '(':
            stack.append(word)
        elif word == '[':
            stack.append(word)
        elif word == ')':
            if not stack:
                print('no')
                continue
            elif stack[len(stack)-1] == '(':
                stack.pop()
            else:
                print('no')
                continue
        elif word == ']':
            if not stack:
                print('no')
                continue
            elif stack[len(stack)-1] == '[':
                stack.pop()
            else:
                print('no')
                continue
    if not stack:
        print("yes")
