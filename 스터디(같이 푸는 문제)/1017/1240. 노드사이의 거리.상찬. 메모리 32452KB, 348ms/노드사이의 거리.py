import sys
from collections import deque

def bfs(n, m):
    q = deque([[n, 0]])                                 # 출발 지점과 초기거리 0 지정
    visited = [0] * (N + 1)                             # 방문기록을 통해 목표지점까지의 거리 저장
    while q:
        x, x_dist = q.popleft()
        if x == m:                                      # 다음 방문 위치가 목적지일 경우 거리를 출력하고 종료
            print(visited[x])
            break
        for y, dist in adjList[x]:                      # 인접 노드들을 탐색 진행
            if visited[y] == 0:
                visited[y] = visited[x] + dist          # 거리를 더해줌
                q.append([y, dist])

N, M = map(int, sys.stdin.readline().split())
adjList = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v, w = map(int, sys.stdin.readline().split())
    adjList[u].append([v, w])
    adjList[v].append([u, w])
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    bfs(s, e)