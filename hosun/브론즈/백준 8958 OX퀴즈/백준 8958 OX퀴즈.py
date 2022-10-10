import sys
sys.stdin = open('input.txt')

T = int(input())

for H in range(T):
    arr = list(input())
    N = len(arr)
    memo = [0] * N
    if arr[0] == 'O':
        memo[0] += 1
    for i in range(1, N):
        if arr[i] == 'O':
            memo[i] += (memo[i - 1] + 1)
    print(sum(memo))