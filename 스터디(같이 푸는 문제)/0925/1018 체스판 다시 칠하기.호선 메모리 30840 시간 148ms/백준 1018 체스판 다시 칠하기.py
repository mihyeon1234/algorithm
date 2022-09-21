import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

chess = list(input() for _ in range(N))
mini = N * M // 2
for i in range(N - 7):
    for j in range(M - 7):
        for m in range(2):
            change = 0
            if m == 0:
                for k in range(8):
                    check = list(chess[i + k][j:j + 8])
                    for l in range(8):
                        if k % 2 == 0:
                            if l % 2 == 0:
                                if check[l] == 'W':
                                    continue
                                else:
                                    check[l] = 'W'
                                    change += 1
                            else:
                                if check[l] == 'B':
                                    continue
                                else:
                                    check[l] = 'B'
                                    change += 1
                        else:
                            if l % 2 == 0:
                                if check[l] == 'B':
                                    continue
                                else:
                                    check[l] = 'B'
                                    change += 1
                            else:
                                if check[l] == 'W':
                                    continue
                                else:
                                    check[l] = 'W'
                                    change += 1

                if mini > change:
                    mini = change
            else:
                for k in range(8):
                    check = list(chess[i + k][j:j + 8])
                    for l in range(8):
                        if k % 2 == 0:
                            if l % 2 == 0:
                                if check[l] == 'B':
                                    continue
                                else:
                                    check[l] = 'B'
                                    change += 1
                            else:
                                if check[l] == 'W':
                                    continue
                                else:
                                    check[l] = 'W'
                                    change += 1
                        else:
                            if l % 2 == 0:
                                if check[l] == 'W':
                                    continue
                                else:
                                    check[l] = 'W'
                                    change += 1
                            else:
                                if check[l] == 'B':
                                    continue
                                else:
                                    check[l] = 'B'
                                    change += 1

                if mini > change:
                    mini = change
print(mini)