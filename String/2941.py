# 크로아티아 알파벳
import sys
word = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

N = sys.stdin.readline().rstrip()

for i in word:
    if i in N:
        N = N.replace(i, ' ')  # 단순하게 카운트 세니까 2개 이상못셈.
        # 그래서 찾은 문자를 그냥 띄어쓰기 시켜서, 리스트 길이를 셌다

print(len(N))
