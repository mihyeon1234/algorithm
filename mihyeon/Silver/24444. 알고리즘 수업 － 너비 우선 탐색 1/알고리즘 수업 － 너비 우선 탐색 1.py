from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[]for _ in range(n+1)]
visited = [0]*(n+1)
count = 1

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    global count
    q = deque([r])
    visited[r] = 1
    while q:
        v = q.popleft()
        graph[v].sort()
        for i in graph[v]:
            if visited[i] == 0:
                count += 1
                visited[i] = count
                q.append(i)

bfs(r)

for v in visited[1:]:
    print(v)