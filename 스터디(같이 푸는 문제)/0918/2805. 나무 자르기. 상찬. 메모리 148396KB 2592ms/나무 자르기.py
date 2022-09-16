import sys

N, M = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
end = max(li)                                   # 가장 최대값 추출하여 끝점으로 설정
if end - M > 0:
    start = end - M
else:
    start = 1                                       # 1이 가장 최소값이므로 시작점으로 설정
while start <= end:
    rest = 0
    mid = (start + end) // 2
    for i in li:
        if i > mid:
            rest += i - mid
            if rest > M:                        # 중간에 더하면서 M보다 커지면 break로 백트래킹
                break
    if rest > M:
        start = mid + 1
    elif rest < M:
        end = mid - 1
    else:
        print(mid)                              # 구하려는 값과 동일하면 값 출력
        break
else:                                           # 끝까지 구해지지 않을 시 개수가 부족해서 end가 -1되면서 종료됨
    print(end)

'''
3 8
20 15 14
'''