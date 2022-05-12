# BOJ 1874
# 스택 수열

n = int(input())
arr = list(int(input()) for _ in range(n))
stack = []
ans = []
index = 0

for i in range(1, n + 1):
    stack.append(i)
    ans.append("+")

    while stack and arr[index] == stack[-1]:
        stack.pop()
        ans.append("-")
        index += 1

if stack:  # 리스트 비어있다면
    print("NO")
else:
    print("\n".join(ans))
