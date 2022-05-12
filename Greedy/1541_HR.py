# BOJ 1439
# 뒤집기

s = input()
zero, one = 0, 0

for x in range(len(s) - 1):
    if s[x] != s[x + 1]:
        if s[x] == "0":
            one += 1
        else:
            zero += 1
print(max(zero, one))
