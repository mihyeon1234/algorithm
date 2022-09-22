import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline()) for _ in range(N)]
A = 'BWBWBWBW'
B = 'WBWBWBWB'
minV = 64
for r in range(N - 7):
    for c in range(M - 7):
        cnt_BW = cnt_WB = 0
        for chess_r in range(8):
            for chess_c in range(8):
                if chess_r % 2 == 0:            # BW로 시작하는 체스판
                    if board[r + chess_r][c + chess_c] != A[chess_c]:   # 다른 문양일 경우 1증가
                        cnt_BW += 1
                    else:                       # WB로 시작하는 체스판
                        cnt_WB += 1
                else:                           # BW로 시작하는 체스판      
                    if board[r + chess_r][c + chess_c] != B[chess_c]:   # 다른 문양일 경우 1증가
                        cnt_BW += 1
                    else:                       # WB로 시작하는 체스판
                        cnt_WB += 1
        if minV > min(cnt_BW, cnt_WB):
            minV = min(cnt_BW, cnt_WB)
print(minV)