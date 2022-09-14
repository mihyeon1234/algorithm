import sys
sys.stdin = open('input.txt')


def f(i, L):
    if i == L:
        ans = []
        for i in range(L):
            if bit[i]:
                ans.append(lst[i])
        if len(ans) == M:
            print(*ans)
    else:
        bit[i] = 1
        f(i+1, L)
        bit[i] = 0
        f(i+1, L)


N, M = map(int, input().split())
lst = list(_ for _ in range(1, N + 1))
bit = [0] * N
f(0, N)
