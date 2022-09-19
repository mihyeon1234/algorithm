import sys
sys.stdin = open('input.txt')


def f(x):
    for i in range(3, x + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[-1]


n = int(input())
if n == 1:
    print(1)
else:
    memo = [-1] * (n + 1)
    memo[0] = 0
    memo[1] = 1
    memo[2] = 2
    print(f(n) % 10007)