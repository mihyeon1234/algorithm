import sys
sys.stdin = open('input.txt')

bingo = list(list(map(int, input().split())) for _ in range(5))
turn = list(list(map(int, input().split())) for _ in range(5))
bb = []
for i in bingo:
    for j in i:
        bb.append(j)
tt = []
for i in turn:
    for j in i:
        tt.append(j)
cnt = 0
for k in tt:
    i = bb.index(k) // 5
    j = bb.index(k) % 5
    bingo[i][j] = 0
    if i == j:
        if bingo[i][j] == bingo[(i + 1) % 5][(i + 1) % 5] == bingo[(i + 2) % 5][(i + 2) % 5] == bingo[(i + 3) % 5][(i + 3) % 5] == bingo[(i + 4) % 5][(i + 4) % 5] == 0:
            cnt += 1
            if cnt == 3:
                print(tt.index(k) + 1)
                break
    if i + j == 4:
        if bingo[i][j] == bingo[(i + 1) % 5][4 -((i + 1) % 5)] == bingo[(i + 2) % 5][4 - ((i + 2) % 5)] == bingo[(i + 3) % 5][4 - ((i + 3) % 5)] == bingo[(i + 4) % 5][4 - ((i + 4) % 5)] == 0:
            cnt += 1
            if cnt == 3:
                print(tt.index(k) + 1)
                break
    if bingo[i].count(0) == 5:
        cnt += 1
        if cnt == 3:
            print(tt.index(k) + 1)
            break
    if bingo[i][j] == bingo[(i + 1) % 5][j] == bingo[(i + 2) % 5][j] == bingo[(i + 3) % 5][j] == bingo[(i + 4) % 5][j] == 0:
        cnt += 1
        if cnt == 3:
            print(tt.index(k) + 1)
            break