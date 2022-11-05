from collections import deque
import heapq
'''
출입구마다 함수 실행을 통해 산봉우리까지의 intensity 갱신 진행
visited를 활용해서 방문기록 남기기
가는 길마다 가중치를 비교해서 max값만 들고 지나가기
단, 산봉우리에서는 그 가중치들 중에서 min값을 기록한다.
다시 돌아오는 길은 같은 루트로 돌아오면 되기 때문에 다시 구할 필요는 없다.
'''

def solution(n, paths, gates, summits):
    adjList = [[] for _ in range(n + 1)]    # 각각의 간선에 대한 정보 기록
    gate_dict = set(gates)                  # 출입구 기록
    summits_dict = set(summits)             # 산봉우리 기록

    for i in paths:
        v, u, w = i
        adjList[v].append([u, w])
        adjList[u].append([v, w])

    peak = n + 1
    total_minV = 100000000                  # 전체 값 중에서 가장 작은 intensity를 기록해준다.
    visited = [100000000] * (n + 1)
    for z in gates:                         # 각각의 게이트에서 탐색 진행
        q = []                              # 가장 작은 케이스 먼저 시작해서 백트래킹이 될 수 있게 한다. 다익스트라 느낌
        heapq.heappush(q, [0, z])
        while q:
            maxV, x = heapq.heappop(q)
            if maxV > total_minV:           # 최소 intensity보다 크면 더 이상 진행할 필요가 없으므로 continue
                continue
            for n_x, n_maxV in adjList[x]:  # 주변 탐색 진행
                temp_maxV = maxV
                if n_x in gate_dict:        # 출입구이면 탐색 X
                    continue
                if n_maxV > temp_maxV:      # 가야하는 가중치가 더 클 경우 해당 크기로 진행해야하므로
                    temp_maxV = n_maxV      # intensity 갱신
                if n_x in summits_dict:     # 봉우리일 경우
                    if visited[n_x] > temp_maxV:  # 가장 작은 값으로 계속 갱신
                        visited[n_x] = temp_maxV
                        if total_minV > temp_maxV:  # 산봉우리의 값이 전체 intensity보다 작은 경우 갱신
                            total_minV = temp_maxV
                            peak = n_x
                        elif total_minV == temp_maxV and peak > n_x:    # 같은 경우에는 산봉우리가 값이 작은 녀석으로 갱신
                            peak = n_x
                else:
                    if visited[n_x] > temp_maxV and temp_maxV <= total_minV:
                        visited[n_x] = temp_maxV
                        heapq.heappush(q, [temp_maxV, n_x])


    result = [peak, total_minV]

    return result