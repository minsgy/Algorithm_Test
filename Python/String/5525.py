# IOIOI
import sys
N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
S = sys.stdin.readline().rstrip()

answer = 0
count = 0
i = 1

while i < M - 1:
    if S[i-1] == "I" and S[i] == "O" and S[i+1] == "I":
        count += 1
        if count == N:
            count -= 1
            answer += 1
        i += 1
    else:
        count = 0
    i += 1

print(answer)
