import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

# 방문 가능한 총 노드의 개수를 파악한 후 그 개수의 -1을 해준 다음 *2를 해준 값이 바로 해답이다
# 해당 노드들을 모두 왕복으로 이동해야하므로 위와 같이 진행된다.
# DFS를 통해 리프 노드부터 들어올 예정이며 그 거리가 D보다 큰 경우의 노드를 카운트 한다
# 여러 줄에서 들어오는 경우 해당 길이를 모두 확인해서 D보다 큰 경우의 노드에 더해주고 가장 큰값은 그대로 그 값을 들고 진행된다
# 가장 큰값은 나중에 노드의 개수로 변환 예정


def dfs(n):
    global cnt
    if n != S and len(adjList[n]) == 1:             # 시작점이 아니고 움직일 수 있는 간선의 개수가 1개이면 리프 노드이므로 길이 0부터 시작
        return 0
    else:
        data = []                                   # 여러 갈래로 들어오는 길이를 담을 저장 리스트
        for w in adjList[n]:
            if visited[w] == 0:
                visited[w]= 1
                distance = dfs(w) + 1               # 그 전 길이의 1만큼 이동한 거리가 들어온다.
                data.append(distance)
        maxV = max(data)                            # 들어오는 길이의 가장 큰 값을 확인하고
        if len(data) >= 2:                          # 여러 갈래에서 들어왔을 경우에는 그 값들을 모두 비교해 D보다 큰값을 세어준다.
            for j in data:
                if j > D and j != maxV:             # 이때 max값은 나중에 계산할 예정이므로 무시하고 넘어가고 아닌 경우만 센다.
                    cnt += j - D
            if maxV > D:                            # max인 값이 여러 개 일수도 있으니 그 경우를 세어준다.
                cnt += (data.count(maxV) - 1) * (maxV - D)
        return maxV

N, S, D = map(int, input().split())             # 노드의 개수, 시작 위치, 힘
adjList = [[] for _ in range(N + 1)]            # 인접 리스트
visited = [0] * (N + 1)                         # 방문기록
for _ in range(N - 1):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)
cnt = 0                                     # 가야하는 총 노드의 개수
visited[S] = 1                              # 시작점은 방문 기록
if N == 1:                                  # 개수가 하나인 경우 움직이지 않아도 되므로 0을 출력
    print(0)
else:
    root = dfs(S)                           # 시작점에서의 Max값을 가져옴
    if root > D:                            # D보다 큰 경우에는 root의 값에서 D를 뺀 값을 더해줘야한다.
        cnt += root - D                     # 가장 긴 길이를 처리해야하기 때문이다.
        print(cnt * 2)
    else:
        print(0)                            # 만약 D보다 작거나 같은 경우에는 움직일 필요가 없으므로 0 출력