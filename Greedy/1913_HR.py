# BOJ 1913
# 회의실 배정

n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))
meeting.sort(key=lambda x: (x[1], x[0]))  # 끝나는 순서대로 정렬

cnt, endT = 0, 0  # -> cnt를 1로 두면 x(무조건 첫번째 회의가 시작된다고 가정하지 말기)
for (s, e) in meeting:
    if s >= endT:
        cnt += 1
        endT = e
print(cnt)
