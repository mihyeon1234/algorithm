import sys
sys.stdin = open('input.txt')


def f(n, lst):
    global minus
    global zero
    global plus
    num = n // 3
    for i in range(0, n, num):
        for j in range(0, n, num):
            piece = []
            good = 0
            for k in range(i, i + num):
                piece.append(lst[k][j:j + num])
                if piece[0] == piece[-1]:
                    good += 1
            if good == num:
                if piece[0].count(piece[0][0]) == num:
                    if piece[0][0] == -1:
                        minus += 1
                    elif piece[0][0] == 0:
                        zero += 1
                    else:
                        plus += 1
                else:
                    f(num, piece)
            else:
                f(num, piece)


N = int(sys.stdin.readline())
paper = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
minus = 0
zero = 0
plus = 0
if paper.count(paper[0]) == N:
    if paper[0][0] == -1:
        minus += 1
    elif paper[0][0] == 0:
        zero += 1
    else:
        plus += 1
else:
    f(N, paper)
print(minus)
print(zero)
print(plus)