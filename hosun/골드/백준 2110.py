import sys
sys.stdin = open('input.txt')

N, C = map(int, input().split())
lst = []
for H in range(N):
    X = int(input())
    lst.append(X)
lst
cnt = C
for i in range(C):

