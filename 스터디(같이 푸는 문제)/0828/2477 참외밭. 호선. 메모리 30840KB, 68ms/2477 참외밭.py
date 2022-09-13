import sys
sys.stdin = open('input.txt')

K = int(input())
lst = list(tuple(map(int, input().split())) for _ in range(6))
row = 0
column = 0
m_row = 0
m_column = 0
for i in lst:
    if i[0] == 1:
        if
