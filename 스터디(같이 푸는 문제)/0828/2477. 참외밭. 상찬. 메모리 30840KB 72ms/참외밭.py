N = int(input())
li = [list(map(int, input().split())) for _ in range(6)]

D = [1, 4, 2, 3]                                # 방향 순환
d = D.index(li[0][0]) - 1                       # 첫 출발의 방향 위치
maxc = maxr = del_a = 0                         # 큰 사각형과 빼주어야 할 사각형 넓이를 입력할 변수
flag = False                                    # 방향 순환 실패 시의 신호
for i in range(6):
    d = (d + 1) % 4                             # 방향 순환 체크
    if li[i][0] != D[d] and flag == False:      # 방향 순환 실패 시 해당 위치가 내부에서 꺽이는 부분
        del_a = li[i][1] * li[i - 1][1]         # 해당 점의 길이와 그 전 점의 길이의 곱은 삭제해야할 부분
        flag = True                             # 점을 찾은 순간 flag 신호 변경
        
    if li[i][0] == 1 or li[i][0] == 2:          # 1, 2의 방향 시 전체 면적의 가로 길이
        if li[i][1] > maxr:
            maxr = li[i][1]
    else:                                       # 3, 4의 방향 시 전체 면적의 가로 길이
        if li[i][1] > maxc:
            maxc = li[i][1]

if flag == False:                               # 방향 순환 미 실패 시 첫 좌표가 꺽이는 부분
    del_a = li[0][1] * li[-1][1]

print((maxr * maxc - del_a) * N)