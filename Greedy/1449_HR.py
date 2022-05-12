# BOJ 1449
# 수리공 항승

n, l = map(int, input().split())
point = list(map(int, input().split()))
point.sort()
cnt = 1
loc = point[0] + l - 1
for i in range(n):
    if point[i] <= loc:
        continue
    else:
        loc = point[i] + l - 1
        cnt += 1
print(cnt)
