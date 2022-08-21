import sys
sys.stdin = open('input.txt')

N = int(input())

lst = list([0] * 101 for _ in range(101))
for T in range(1, N + 1):
    x1, y1, row, column = map(int, input().split())
    for y in range(y1, y1 + column):
        for x in range(x1, x1 + row):
            lst[y][x] = T
for i in range(1, N + 1):
    cnt = 0
    for j in lst:
        cnt += j.count(i)
    print(cnt)