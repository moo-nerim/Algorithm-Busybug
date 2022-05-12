# BOJ 1339
# 단어 수학

n = int(input())

str = []
ans = []
num = 0

for i in range(n):
    str.append(input())
    num += len(input())
alpha = [""] * num
str.sort(reverse=True)  # 가장 긴 문자열 순으로 정렬

k = 1
while k != 0:
    remove = str.pop()[0]  # 가장 큰 자릿수 문자

    for j in range(num - 1, 0, -1):
        print(alpha[j])
        if alpha[j] == remove:
            continue
        elif alpha[j] == "":
            alpha[j] = remove
    str.sort(reverse=True)
    k += 1

print(alpha)
