# BOJ 4796
# 캠핑

cnt = 1
res = 0

while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    else:
        res = (L + V // P * L) if (V % P > L) else (V % P + V // P * L)
        print("Case %d: %d" % (cnt, res))
    cnt += 1
