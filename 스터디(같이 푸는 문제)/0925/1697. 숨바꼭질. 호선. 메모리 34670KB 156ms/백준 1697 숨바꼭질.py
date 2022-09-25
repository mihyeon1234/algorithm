import sys
from collections import deque
sys.stdin = open('input.txt')


def f():
    go = deque()
    go.append(N)
    while go:
        ans = go.popleft()
        if ans == K:
            print(visit[ans])
            break
        else:
            lst = [ans + 1, ans - 1, ans * 2]
            for i in lst:
                if 0 <= i <= MM:
                    if visit[i] == 0:
                        visit[i] = visit[ans] + 1
                        go.append(i)


N, K = map(int, input().split())
MM = 100000
visit = [0] * (MM + 1)
f()

