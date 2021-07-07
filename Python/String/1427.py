# 소트인사이드

n = list(map(int, input()))

n.sort(reverse=True)

for i in n:
    print(i, end='', flush=True)
