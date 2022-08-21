N = int(input())
maxV = 0                            # 최대 개수를 넣을 변수
max_li = []                         # 최대 개수일 때의 집합을 넣을 변수

for n in range(N, 0, -1):           # 끝자리부터 진행
    li = [N, n]
    
    while li[-1] >= 0:
        li.append(li[-2] - li[-1])  # 음수가 나올 때까지 문제의 조건에 맞는 행위 반복
    cnt = len(li)
    if maxV < cnt - 1:                      # maxV 계속해서 탐색 진행
        maxV = cnt - 1
        max_li = li
print(maxV)
print(*max_li[:maxV])
    