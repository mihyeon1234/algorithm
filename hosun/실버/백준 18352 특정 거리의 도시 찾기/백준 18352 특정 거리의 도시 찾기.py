import sys
from collections import deque


sys.stdin = open('input.txt')


def f(x, k):
    global ans
    q = deque()
    q.append(x)
    while q:
        t = q.popleft()
        if visit[t] == k:
            ans.append(t)
        else:
            for w in arr[t]:
                if visit[w] == -1:
                    visit[w] = visit[t] + 1
                    q.append(w)


N, M, K, X = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(N + 1)]
visit = [-1] * (N + 1)
visit[X] = 0
ans = []
for H in range(M):
    A, B = map(int, sys.stdin.readline().split())
    arr[A].append(B)
f(X, K)
ans.sort()
if len(ans) >= 1:
    for i in ans:
        print(i)
else:
    print(-1)