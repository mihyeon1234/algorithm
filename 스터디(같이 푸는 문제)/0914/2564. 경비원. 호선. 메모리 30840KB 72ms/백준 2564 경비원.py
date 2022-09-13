import sys
sys.stdin = open('input.txt')

row, column = map(int, input().split())
N = int(input())
lst = []
for i in range(N):
    shop = list(map(int, input().split()))
    lst.append(shop)

X_drc, X_dis = map(int, input().split())

dis = 0
for i in lst:
    if X_drc == 1:
        if i[0] == 1:
            dis += abs(X_dis - i[1])
        elif i[0] == 2:
            if X_dis + i[1] < (row - X_dis) + (row - i[1]):
                dis += ((X_dis + i[1]) + column)
            else:
                dis += (((row - X_dis) + (row - i[1])) + column)
        elif i[0] == 3:
            dis += (X_dis + i[1])
        else:
            dis += ((row - X_dis) + i[1])
    elif X_drc == 2:
        if i[0] == 2:
            dis += abs(X_dis - i[1])
        elif i[0] == 1:
            if X_dis + i[1] < (row - X_dis) + (row - i[1]):
                dis += ((X_dis + i[1]) + column)
            else:
                dis += (((row - X_dis) + (row - i[1])) + column)
        elif i[0] == 3:
            dis += (X_dis + (column - i[1]))
        else:
            dis += ((row - X_dis) + (column - i[1]))
    elif X_drc == 3:
        if i[0] == 3:
            dis += abs(X_dis - i[1])
        elif i[0] == 4:
            if X_dis + i[1] < (column - X_dis) + (column - i[1]):
                dis += ((X_dis + i[1]) + row)
            else:
                dis += (((column - X_dis) + (column - i[1])) + row)
        elif i[0] == 1:
            dis += (X_dis + i[1])
        else:
            dis += ((column - X_dis) + i[1])
    elif X_drc == 4:
        if i[0] == 4:
            dis += abs(X_dis - i[1])
        elif i[0] == 3:
            if X_dis + i[1] < (column - X_dis) + (column - i[1]):
                dis += ((X_dis + i[1]) + row)
            else:
                dis += (((column - X_dis) + (column - i[1])) + row)
        elif i[0] == 1:
            dis += (X_dis + (row - i[1]))
        else:
            dis += ((column - X_dis) + (row - i[1]))
print(dis)