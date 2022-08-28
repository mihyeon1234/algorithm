import sys

N, K = map(int, sys.stdin.readline().split())
num_li = list(map(int, sys.stdin.readline().split()))

maxV = start = sum(num_li[:K])                          # 초기값 설정

for i in range(1, N - K + 1):
    start = start - num_li[i - 1] + num_li[i + K - 1]   # 하나씩 더하고 빼는 형식으로 모든 값을 확인
    if start > maxV:
        maxV = start
print(maxV)