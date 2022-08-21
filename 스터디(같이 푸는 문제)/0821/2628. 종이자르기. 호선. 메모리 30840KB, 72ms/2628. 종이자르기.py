import sys
sys.stdin = open('input.txt')

row, column = map(int, input().split())
T = int(input())
lst = list([0] * row for _ in range(column))
lst_row = []
lst_column = []

for H in range(1, T + 1):
    A, B = map(int, input().split())
    if A == 0:
        lst_column.append(B)
    else:
        lst_row.append(B)

lst_row.sort()
lst_column.sort()
lst_row.insert(0, 0)
lst_row.append(row)
lst_column.insert(0, 0)
lst_column.append(column)
max_row = 0
max_column = 0
for i in range(len(lst_row) - 1):
    if lst_row[i + 1] - lst_row[i] > max_row:
        max_row = lst_row[i + 1] - lst_row[i]
for i in range(len(lst_column) - 1):
    if lst_column[i + 1] - lst_column[i] > max_column:
        max_column = lst_column[i + 1] - lst_column[i]
print(max_row * max_column)
