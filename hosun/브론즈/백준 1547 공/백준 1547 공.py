import sys
sys.stdin = open('input.txt')

T = int(input())
lst = [1, 2, 3]
for H in range(T):
    X, Y = map(int, input().split())
    lst[X - 1], lst[Y - 1] = lst[Y - 1], lst[X - 1]
print(lst.index(1) + 1)