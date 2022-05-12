# BOJ 3098
# 소셜네트워크

n, m = map(int, input().split())
arr = list([0]*n for _ in range(n))
k = list()
day = 0
for _ in range(m):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1
    arr[a-1][a-1] = 1
    arr[b-1][b-1] = 1
while (True):
    cnt = 0
    for i in range(n):
        for j in range(i+1, 5):
            if arr[i][j] == 0:
                arr[i][j] = 1
                arr[j][i] = 1
                cnt += 1
                break
    if arr[0].count(0) == 1 and arr[n-1].count(0) == 1 and arr[0][n-1] == 0 and arr[n-1][0] == 0:
        k.append(cnt+1)
        break
    k.append(cnt)
print(len(k))
for x in k:
    print(x)
