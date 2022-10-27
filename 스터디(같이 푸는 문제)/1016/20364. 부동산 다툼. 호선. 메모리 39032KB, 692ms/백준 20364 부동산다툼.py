import sys

N, Q = map(int, sys.stdin.readline().split())
visit = [0] * (N + 1)
for _ in range(Q):
    want = check = int(sys.stdin.readline())
    ori = 0
    while check != 1:
        if visit[check] == 1:
            ori = check
        check //= 2
    if ori == 0:
        visit[want] = 1
        print(0)
    else:
        print(ori)