import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
num = list(map(int, input().split()))
M_total = -9999999
total = 0
first = 0
for i in range(N):
    total += num[i]
    if i >= K - 1:
        M_total = max(M_total, total)
        total -= num[first]
        first += 1
print(M_total)