import sys
from collections import deque

def bfs():                                      # bfs를 통해 토마토 익어가게 만들기
    while q:
        rs, cs = q.popleft()
        for d in range(6):
            nr = rs + dr[d]
            nc = cs + dc[d]
            if 0 <= nr < total_H and 0 <= nc < M and tomato[nr][nc] == 0:
                tomato[nr][nc] = tomato[rs][cs] + 1
                q.append((nr, nc))

input = sys.stdin.readline
M, N, H = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N * H)]
q = deque()
for block in range(N * H, -1, -N):              # 1을 각 층의 구분을 위해 삽입
    tomato.insert(block, [1] * M)
total_H = len(tomato)
for r in range(total_H):                        # 1이 있는 위치를 확인
    for c in range(M):
        if tomato[r][c] == 1 and r % (N + 1) != 0:
            q.append((r, c))
dr = [0, 1, 0, -1, N + 1, - N - 1]              # 총 6가지의 델타에 대해 입력
dc = [1, 0, -1, 0, 0, 0]
bfs()
total_max = max(map(max, tomato))
total_min = min(map(min, tomato))
flag = True
for r1 in tomato:
    if 0 in r1:
        flag = False
if total_max == total_min == 1:
    print(0)
elif flag == False:
    print(-1)
elif flag == True:
    print(total_max - 1)


==================================================================================

def bfs():
    while q:
        rs, cs, hs = q.popleft()
        for d in range(6):
            if 0 <= d < 4:              # 2차원 공간에서의 bfs 진행
                nr = rs + dr[d]
                nc = cs + dc[d]
                if 0<= nr < N and 0 <= nc < M and tomato[hs][nr][nc] == 0:
                    tomato[hs][nr][nc] = tomato[hs][rs][cs] + 1
                    q.append([nr, nc, hs])
            else:
                nh = hs + dr[d]         # 3차원 공간에서의 bfs 진행
                if 0 <= nh < H and tomato[nh][rs][cs] == 0:
                    tomato[nh][rs][cs] = tomato[hs][rs][cs] + 1
                    q.append([rs, cs, nh])


M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
dr = [0, 1, 0, -1, -1, 1]               # 3차원 공간에 대한 델타 정보 입력(0 ~ 3까지는 2차원 4 ~ 5는 3차원)
dc = [1, 0, -1, 0, 0, 0]
q = deque()
for h in range(H):
    for r in range(N):
        for c in range(M):
            if tomato[h][r][c] == 1:    # 1이 있는 위치 저장
                q.append([r, c, h])
bfs()
day = -1
flag = True
for i in tomato:
    maxV = max(map(max, i))             # 최종 날짜 확인을 위해 각 층마다 max의 값을 확인!!!
    if day < maxV:
        day = maxV
    for j in i:
        if 0 in j:                      # 0 발견 시 break하여 -1을 출력
            flag = False
            break
    if not flag:
        break
if flag:
    print(day - 1)
else:
    print(-1)