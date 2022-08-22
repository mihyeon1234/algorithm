def check1(board):
    check = 0                                   # 빙고 카운트 변수
    cnt_xl = 0                                  # 대각선 왼쪽에서 아래 변수
    cnt_xr = 0                                  # 대각선 오른쪽에서 왼쪽 아래 변수
    for r in range(5):
        cnt_c = 0
        if board[r][ : 5] == [0] * 5:           # 가로에 대한 빙고 확인 조건
            check += 1
        if board[r][r] == 0:                    # 대각선 왼쪽 빙고 확인
            cnt_xl += 1
        if board[r][4 - r] == 0:                # 대각선 오른쪽 빙고 확인
            cnt_xr += 1

        for c in range(5):
            if board[c][r] == 0:                # 세로 방향 빙고 확인
                cnt_c += 1
        if cnt_c == 5:                          # 모두 0이 5개이면 check 1씩 증가
            check += 1
    if cnt_xr == 5:
        check += 1
    if cnt_xl == 5:
        check += 1
    return check

board = [list(map(int, input().split())) for _ in range(5)]
choose = []
for _ in range(5):
    choose.extend(list(map(int, input().split())))  # extend는 리스트를 풀고 받아줘서 좋음

for i in range(len(choose)):                        # 같은 값을 가지는 경우 0으로 변경
    for j in board:
        if choose[i] in j:
            idx = j.index(choose[i])
            j[idx] = 0
            break

    cnt_bingo = check1(board)                       # 빙고 3이상일 경우 출력 후 종료
    if cnt_bingo >= 3:
        print(i + 1)
        break