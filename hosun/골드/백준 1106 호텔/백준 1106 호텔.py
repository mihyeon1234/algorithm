import sys

C, N = map(int, sys.stdin.readline().split())
lst = []
visit = [0] + [99999999] * (C + 99)
for _ in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))
lst.sort()
for x, y in lst:
    for i in range(y, C + 100):
        visit[i] = min(visit[i - y] + x, visit[i])
print(min(visit[C:]))