import sys
sys.stdin = open('input.txt')


def f(x):
    global visit
    q = []
    q.append(x)
    visit[x] = 1
    if len(q) == 0:
        return
    while q:
        v = q.pop(0)
        for w in lst[v]:
            if visit[w] == 0:
                visit[w] = 1
                q.append(w)


V = int(input())
E = int(input())
lst = [[] for _ in range(V + 1)]
visit = [0] * (V + 1)
for _ in range(E):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

f(1)
print(visit.count(1) - 1)