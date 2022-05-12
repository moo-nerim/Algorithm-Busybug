# BOJ 1543
# 문서 검색

str = input()
findStr = input()

res = str.split(findStr)
print(len(res) - 1)
