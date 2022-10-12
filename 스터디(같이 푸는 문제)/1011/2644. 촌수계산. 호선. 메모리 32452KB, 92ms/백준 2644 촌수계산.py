from collections import deque
import sys


def f(x, y):
    global ans
    q = deque()
    q.append(x)
    visit = [0] * (n + 1)
    while q:
        v = q.popleft()
        if v == y:
            ans = visit[v]
            return
        for w in memo[v]:
            if visit[w] == 0:
                q.append(w)
                visit[w] = visit[v] + 1
    return


n = int(sys.stdin.readline())
start, end = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
memo = [[] for _ in range(n + 1)]
ans = -1
for i in lst:
    memo[i[0]].append(i[1])
    memo[i[1]].append(i[0])
f(start, end)
print(ans)
