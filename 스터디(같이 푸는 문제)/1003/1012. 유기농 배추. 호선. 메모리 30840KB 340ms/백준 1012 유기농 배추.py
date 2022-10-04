import sys
sys.stdin = open('input.txt')

T = int(input())
for H in range(T):
    M, N, K = map(int, input().split())
    farm = list([0] * (M + 2) for _ in range(N + 2))
    kimchi = list(list(map(int, input().split())) for _ in range(K))
    cnt = 0
    for i in kimchi:
        farm[i[1] + 1][i[0] + 1] = 1
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if farm[i][j] == 1:
                cnt += 1
                farm[i][j] = 0
                dr = [[i + 1, j], [i, j + 1], [i - 1, j], [i, j - 1]]
                while len(dr) > 0:
                    a, b = dr.pop()
                    if farm[a][b] == 1:
                        farm[a][b] = 0
                        dr.append([a + 1, b])
                        dr.append([a, b + 1])
                        dr.append([a - 1, b])
                        dr.append([a, b - 1])
    print(cnt)