import sys
N, M, B = map(int, sys.stdin.readline().split())
li = []

for _ in range(N):
    li.extend(map(int, sys.stdin.readline().split()))
    
minT = 500 * 500 * 256                                  # 최대로 걸리는 시간
maxH = 0

for h in range(min(li), max(li) + 1):                   # 각각의 높이에서 채우고 빼는 시간을 구할 예정
    minus_total = plus_total = time = 0                 # 입력을 받을 변수
    for i in li:
        diff = i - h                                    # 높이의 차를 계산
        if diff > 0:
            plus_total += diff                          # 차가 양수이면 plus 변수에 더하고
        elif diff < 0:
            minus_total += diff                         # 차가 음수이면 minus 변수에 더함
            
    if plus_total + B >= -minus_total:                  # 채울 수 있을 때는 시간 계산
        time += - minus_total + plus_total * 2
    else:
        break
    
    if time < minT:                                     # 최소 시간 찾기
        minT = time
        maxH = h
    elif time == minT:
        if h > maxH:
            maxH = h

print(minT, maxH)