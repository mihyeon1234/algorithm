import sys
sys.stdin = open('input.txt')


def f(x, y, z):
    q = []
    q.append([x, y])

    while q:
        v = q.pop(0)
        x = v[0]
        y = v[1]
        if visit[x][y] == 0:
            visit[x][y] = 1
            for w in range(4):
                nx, ny = x + dr[w][0], y + dr[w][1]
                if 0 <= nx < N and 0 <= ny < N:
                    if nemo[nx][ny] == z:
                        q.append([nx, ny])


N = int(sys.stdin.readline())
nemo = [list(sys.stdin.readline()) for _ in range(N)]
dr = [[1, 0], [-1, 0], [0, -1], [0, 1]]

cnt = [0, 0]
for k in range(2):
    visit = [[0] * N for _ in range(N)]
    if k == 1:
        for a in range(N):
            for b in range(N):
                if nemo[a][b] == 'R':
                    nemo[a][b] = 'G'
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                f(i, j, nemo[i][j])
                cnt[k] += 1

print(*cnt, end=' ')