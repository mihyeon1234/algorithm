import sys
sys.stdin = open('input.txt')

C, R = map(int, input().split())
K = int(input())
con = list([-1] + [0] * C + [-1] for _ in range(R))
con.append([-1] * (C + 2))
con.insert(0, [-1] * (C + 2))
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
i = 1
j = 1
dr = 0
ans = 0

for k in range(1, C * R + 1):
    if k == K:
        ans = [j, i]
        break
    con[i][j] = k
    ni = i + di[dr]
    nj = j + dj[dr]
    if 1 <= ni <= R and 1 <= nj <= C and con[ni][nj] == 0:
        i, j = ni, nj
    else:
        dr = (dr + 1) % 4
        i = i + di[dr]
        j = j + dj[dr]
if ans == 0:
    print(ans)
else:
    for t in ans:
        print(t, end=' ')