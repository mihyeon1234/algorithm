N, K = map(int, input().split())
dp = [0] * 100001                                       # 총 범위

for i in range(0, N):                                   # N 숫자 이전의 값들은 -1로만 도달할 수 있다.
    dp[i] = N - i                                       

for j in range(N + 1, K + 2):
    if j % 2 == 0:                                      # 짝수일 경우 2를 나눌 수 있으므로
        dp[j] = min(dp[j - 1] + 1, dp[j // 2] + 1)      # 2로 나눈 경로의 수 + 1과 그 전의 경로의 수 + 1 중 최소값 추출
        dp[j - 1] = min(dp[j] + 1, dp[j - 1])           # 그 전의 경로를 최적화시킴
    else:
        dp[j] = dp[j - 1] + 1                           # 2로 나눌 수 없으므로 그 전의 경로의 수 + 1
        dp[j - 1] = min(dp[j] + 1, dp[j - 1])           # 그 전의 경로를 다시 최적화 진행

print(dp[K])