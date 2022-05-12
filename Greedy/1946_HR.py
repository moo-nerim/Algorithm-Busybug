# BOJ 1946
# 신입 사원

import sys

case = int(sys.stdin.readline())
for i in range(case):
    n = int(input())
    inform = []
    for i in range(n):
        g1, g2 = map(int, sys.stdin.readline().split())
        inform.append((g1, g2))
    inform.sort()  # 서류 점수로 이미 정렬했기 때문에, 서류 점수는 고려할 필요 X
    cnt = 1
    grade = inform[0][1]
    for g1, g2 in inform:
        if grade > g2:
            grade = g2
            cnt += 1
    print(cnt)
