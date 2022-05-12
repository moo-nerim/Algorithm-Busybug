# BOJ 4781
# 사탕 가게

import sys
while True:
    n, m = map(float, sys.stdin.readline().split())
    n = int(n)
    d = [0]*(m+1)
    if n == 0 and m == 0.00:
        break
    m = int(m*100+0.5)
    for _ in range(n):
        c, p = map(float, sys.stdin.readline().split())
        c, p = int(c), int(p*100+0.5)
        for i in range(p, m+1):
            d[i] = max(d[i], d[i-p] + c)
    print(d[m])
