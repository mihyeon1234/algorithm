import sys
from collections import deque


def f(ss):
    global maxx
    q = deque(ss)
    while q:
        v = q.popleft()
        dr = [[v[0] + 1, v[1]], [v[0] - 1, v[1]], [v[0], v[1] + 1], [v[0], v[1] - 1], [v[0] + 1, v[1] + 1], [v[0] + 1, v[1] - 1], [v[0] - 1, v[1] + 1], [v[0] - 1, v[1] - 1]]
        for w in dr:
            if 0 <= w[0] < N and 0 <= w[1] < M and space[w[0]][w[1]] == 0:
                q.append(w)
                space[w[0]][w[1]] = space[v[0]][v[1]] + 1


N, M = map(int, sys.stdin.readline().split())
T = max(N, M)
space = []
shark = []
for a in range(N):
    c = list(map(int, sys.stdin.readline().split()))
    space.append(c)
    for b in range(M):
        if c[b] == 1:
            shark.append([a, b])
ans = 0
f(shark)
for k in space:
    maxx = max(k)
    if ans < maxx:
        ans = maxx
print(ans - 1)
