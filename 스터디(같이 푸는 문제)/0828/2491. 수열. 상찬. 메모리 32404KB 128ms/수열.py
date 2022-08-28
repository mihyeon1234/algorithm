N = int(input())
li = list(map(int, input().split()))

T = len(li)
maxV = upper = lower = 1            # 최댓값 변수, 커질 때와 작아질 때 값을 받을 변수

for i in range(T - 1):
    if li[i + 1] >= li[i]:          # 값이 커질 경우 upper 1증가
        upper += 1
        if upper > maxV:            # 최댓값 계속해서 갱신
            maxV = upper
    else:                           # 이 부분에 갱신을 넣으면 마지막에 감소하지 않을 경우 카운트하지 않아 실패
        upper = 1
    if li[i + 1] <= li[i]:          # 값이 작아질 경우 lower 1증가
        lower += 1
        if lower > maxV:            # 최댓값 갱신
            maxV = lower
    else:
        lower = 1
print(maxV)