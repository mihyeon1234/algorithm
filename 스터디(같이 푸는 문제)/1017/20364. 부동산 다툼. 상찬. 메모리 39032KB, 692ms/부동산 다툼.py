import sys
sys.stdin = open('input.txt')

def find_land(n):
    minV = 2 ** 20 + 1
    flag = True                         # 부동산이 계약된 곳이 있었는지 확인 신호
    while n > 0:                        # 1까지 모두 진행될 때까지
        n = n // 2
        if land[n] == 1:
            flag = False                # 부동산이 산 곳을 방문했을 때 minV 갱신 진행
            if n < minV:
                minV = n
    if flag:
        return 0
    else:
        return minV

N, Q = map(int, sys.stdin.readline().split())
land = [0] * (N + 1)                    # 오리 방문 표시
for _ in range(Q):
    chick = int(sys.stdin.readline())
    if land[chick] == 1:                # 이미 방문했던 곳일 경우
        ans = find_land(chick)          # 만약 위에서 걸리면 걸린 자리를 출력
        if ans:
            print(ans)
        else:
            print(chick)                # 아니라면 이미 방문한 곳을 출력
    else:
        land[chick] = 1                 # 방문 기록 남기기
        print(find_land(chick))