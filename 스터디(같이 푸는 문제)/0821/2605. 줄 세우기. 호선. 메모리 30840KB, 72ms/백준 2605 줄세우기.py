import sys
sys.stdin = open('input.txt')

N = int(input())
P = list(map(int, input().split()))
lst = [0] * N
for i in range(0, N):
    lst.insert(i - P[i], i + 1)
    lst.remove(0)
for i in lst:
    print(i, end=' ')