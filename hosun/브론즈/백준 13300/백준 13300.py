import sys
sys.stdin = open('백준 13300.txt')

N, K = map(int, input().split())
lst = list(list(map(int, input().split())) for _ in range(N))
Y = [0] * 7
X = [0] * 7
cnt = 0
for i in lst:
    if i[0] == 1:
        Y[i[1]] += 1
    else:
        X[i[1]] += 1
for j in range(7):
    if Y[j] % K != 0:
        cnt += (Y[j] // K) + 1
    else:
        cnt += (Y[j] // K)
    if X[j] % K != 0:
        cnt += (X[j] // K) + 1
    else:
        cnt += (X[j] // K)
print(cnt)