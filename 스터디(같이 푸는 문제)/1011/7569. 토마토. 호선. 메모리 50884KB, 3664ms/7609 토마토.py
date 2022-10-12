import sys
from collections import deque


def f(toto):
    q = deque(toto)
    while q:
        now = q.popleft()
        dr = [[now[0] + 1, now[1], now[2]],
              [now[0] - 1, now[1], now[2]],
              [now[0], now[1] + 1, now[2]],
              [now[0], now[1] - 1, now[2]],
              [now[0], now[1], now[2] + 1],
              [now[0], now[1], now[2] - 1]]
        for i in dr:
            if 0 <= i[0] < H and 0 <= i[1] < N and 0 <= i[2] < M and box[i[0]][i[1]][i[2]] == 0:
                box[i[0]][i[1]][i[2]] = box[now[0]][now[1]][now[2]] + 1
                q.append(i)
    return


M, N, H = map(int, sys.stdin.readline().split())
box = []
tomato = []
ans = 0
zero_cnt = 0
maxx = -1
for z in range(H):
    floor = []
    for y in range(N):
        row = list(map(int, sys.stdin.readline().split()))
        floor.append(row)
        for x in range(M):
            if row[x] == 1:
                tomato.append([z, y, x])
            elif row[x] == 0 and zero_cnt == 0:
                zero_cnt += 1
    box.append(floor)
if zero_cnt != 0:
    f(tomato)
    for z in box:
        for y in z:
            if maxx < max(y):
                maxx = max(y)
            if 0 in y:
                maxx = -1
                break
        else:
            continue
        break
    if maxx >= 0:
        maxx -= 1
else:
    maxx = 0

print(maxx)

