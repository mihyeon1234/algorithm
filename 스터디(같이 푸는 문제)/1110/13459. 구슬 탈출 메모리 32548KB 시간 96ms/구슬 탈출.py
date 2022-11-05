import sys
from collections import deque
input = sys.stdin.readline

'''
BFS 문제풀이

핵심: 좌표만을 활용하여 이동경로를 계산 (좌표 저장을 통해 중복 계산 제거)
1. 구슬의 움직임에 대한 함수
2. 움직인 구슬이 구멍에 빠졌는지 혹은 겹쳐진 경우가 있는지 확인해서 따로 처리 진행
'''

def move(r, c, d, cnt_move): #움직임에 대한 함수
    # 벽을 만나거나 구멍이 있을 경우 정지, 단 벽은 미리 살펴보고 있는지 확인한다.
    # 이때 R과 B가 같은 좌표선상에 있으면 겹쳐지게 된다. 추후 처리 예정
    while board[r + dr[d]][c + dc[d]] != '#' and board[r][c] != 'O':    
        r, c = r + dr[d], c + dc[d]
        cnt_move += 1
    return r, c, cnt_move

def check(rR, cR, rB, cB, cnt): # 움직인 후의 좌표에 대한 처리 진행
    global ans
    if cnt == 11:   # 10이하의 움직임으로 제한했으므로 그 이상은 return
        return
    for D in range(4):
        nr_R, nc_R, cnt_R = move(rR, cR, D, 0)  # R 구슬의 움직임
        nr_B, nc_B, cnt_B = move(rB, cB, D, 0)  # B 구슬의 움직임

        if board[nr_B][nc_B] == 'O':            # B 구슬이 빠질 경우 무조건 실패이므로 바로 continue로 넘어간다
            continue
        elif board[nr_R][nc_R] == 'O':          # R 구슬이 구멍에 빠질 경우 cnt +1 
            ans = cnt
            return
        if nr_R == nr_B and nc_R == nc_B:       # 좌표가 같을 경우에는 구슬이 각각 움직인 거리를 비교해 위치 재설정 후 append
            if cnt_R > cnt_B:
                nr_R, nc_R = nr_R - dr[D], nc_R - dc[D]
            elif cnt_R < cnt_B:
                nr_B, nc_B = nr_B - dr[D], nc_B - dc[D]
        if [nr_R, nc_R, nr_B, nc_B] not in visited:
            visited.append([nr_R, nc_R, nr_B, nc_B])
            q.append([nr_R, nc_R, nr_B, nc_B, cnt + 1])
    return


N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
r_R, c_R, r_B, c_B = 0, 0, 0, 0

for i in range(N):                  # B와 R의 좌표 찾기
    for j in range(M):
        if board[i][j] == 'B':
            r_B, c_B = i, j
        elif board[i][j] == 'R':
            r_R, c_R = i, j

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
minV = 100000
ans = 0
visited = []                        # 움직였던 좌표 방문 기록
q = deque()
q.append([r_R, c_R, r_B, c_B, 1])
while q:
    x_R, y_R, x_B, y_B, Cnt = q.popleft()
    check(x_R, y_R, x_B, y_B, Cnt)

if ans > 0:
    print(1)
else:
    print(0)
    
#########################################################################################
'''
DFS 풀이 버전
좌표를 기록하고 R과 B를 움직여준다.
막힐 경우 해당 R과 B의 좌표에 있던 값을 .으로 변경 후 함수가 return된다.
이를 계속 반복하여 진행

비효율적인 면: 좌표의 중복도 모두 살펴보면서 진행되므로 시간이 오래걸린다.
BFS의 약 2.5배 느림 
'''

def marble(r_R, c_R, r_B, c_B, D, cnt):
    global ans
    if cnt == 10:
        return
    if ans == 1:
        return

    for d in range(4):
        if d != D:
            D = d
            board[r_R][c_R] = 'R'
            board[r_B][c_B] = 'B'
            nr_R, nc_R = r_R, c_R
            nr_B, nc_B = r_B, c_B
            enter = 0
            while True:
                hell = hole = flag = False
                temp_nr, temp_rc = nr_R, nc_R
                while True:
                    nr_R += dr[D]
                    nc_R += dc[D]
                    if board[nr_R][nc_R] == '.':
                        if nr_R == r_O and nc_R == c_O:
                            board[temp_nr][temp_rc] = '.'
                            board[nr_R][nc_R] = '.'
                            hole = True
                            break
                        flag = True
                        continue
                    elif board[nr_R][nc_R] == 'B' or board[nr_R][nc_R] == '#':
                        board[temp_nr][temp_rc] = '.'
                        nr_R, nc_R = nr_R - dr[D], nc_R - dc[D]
                        board[nr_R][nc_R] = 'R'
                        break

                temp_nr1, temp_rc1 = nr_B, nc_B
                while True:
                    nr_B += dr[D]
                    nc_B += dc[D]
                    if board[nr_B][nc_B] == '.':
                        if nr_B == r_O and nc_B == c_O:
                            hell = True
                            break
                        flag = True
                        continue
                    elif board[nr_B][nc_B] == 'R' or board[nr_B][nc_B] == '#':
                        board[temp_nr1][temp_rc1] = '.'
                        nr_B, nc_B = nr_B - dr[D], nc_B - dc[D]
                        board[nr_B][nc_B] = 'B'
                        break

                # O를 스쳐갔는지 확인

                if hell:
                    board[temp_nr][temp_rc] = '.'
                    board[nr_R][nc_R] = '.'
                    board[temp_nr1][temp_rc1] = '.'
                    board[nr_B][nc_B] = '.'
                    board[r_R][c_R] = '.'
                    board[r_B][c_B] = '.'
                    break

                if hole:
                    ans = 1
                    return

                if not flag:
                    break

            if ans:
                return
            if hell:
                continue
            marble(nr_R, nc_R, nr_B, nc_B, D, cnt + 1)
            if ans:
                return
            board[temp_nr][temp_rc] = '.'
            board[temp_nr1][temp_rc1] = '.'
            board[nr_R][nc_R] = '.'
            board[nr_B][nc_B] = '.'
            board[r_R][c_R] = '.'
            board[r_B][c_B] = '.'


N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
r_R, c_R, r_B, c_B, r_O, c_O = 0, 0, 0, 0, 0, 0     # 위치 설정
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            r_R, c_R = i, j
        elif board[i][j] == 'B':
            r_B, c_B = i, j
        elif board[i][j] == 'O':
            r_O, c_O = i, j
            board[i][j] = '.'
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
ans = 0
# for i in board:
#     print(i)
marble(r_R, c_R, r_B, c_B, -1, 0)
print(ans)