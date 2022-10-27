import sys
sys.stdin = open('input.txt')


def dfs(arr, v, lst):
    global gr
    lst[v] = 1
    if len(arr[v]) > 1:
        if v == S:
            arr[S].pop()
        for j in arr[v]:
            if lst[j] == 0:
                gr += 1
                dfs(arr, j, lst)


N, S, D = map(int, input().split())
E = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
gr = 0
for i in range(N - 1):
    x, y = map(int, input().split())
    E[x].append(y)
    E[y].append(x)
E[S].append(-1)
dfs(E, S, visited)
print(gr * 2)
