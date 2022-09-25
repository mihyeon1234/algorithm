import sys
sys.stdin = open('input.txt')


def f(x):
    for i in range(5, K + 1):
        if i % 2 == 0:
            memo[i] = memo[i // 2] + 1
        else:
            if memo[i + 1] <= memo[i - 1]:
                memo[i] = memo[i + 1] + 1
            else:
                memo[i] = memo[i - 1] + 1
    return memo[K]


N, K = map(int, input().split())
memo = [0] * 100001
print(f(N))
