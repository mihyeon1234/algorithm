import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
for i in range(N - 1):
    lst[i + 1] += lst[i]
lst.insert(0, 0)
for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    print(lst[B] - lst[A - 1])