import sys
sys.stdin = open('input.txt')

T = int(input())
for H in range(T):
    N = int(input())
    memo = [0] * (N + 2)
    memo[0] = [1, 0]
    memo[1] = [0, 1]
    for i in range(2, N + 1):
        memo[i] = [memo[i - 2][0] + memo[i - 1][0], memo[i - 2][1] + memo[i - 1][1]]
    print(memo[N][0], memo[N][1])