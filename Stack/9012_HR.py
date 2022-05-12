# BOJ 9012
# 괄호

t = int(input())
for _ in range(t):
    str = input()
    stack = []

    for x in str:
        if x == "(":
            stack.append("(")
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(")")
    if not stack:
        print("YES")
    else:
        print("NO")
    stack.clear()
