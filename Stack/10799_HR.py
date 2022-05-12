# BOJ 10799
# 쇠막대기

str = input()
stack = []
cnt = 0

for i in range(len(str)):
    if str[i] == "(":
        stack.append(str[i])
    else:
        # 무조건 여는 괄호부터 시작됨
        stack.pop()
        if str[i - 1] == "(":  # 레이저인 경우
            cnt += len(stack)
        else:
            cnt += 1
print(cnt)
