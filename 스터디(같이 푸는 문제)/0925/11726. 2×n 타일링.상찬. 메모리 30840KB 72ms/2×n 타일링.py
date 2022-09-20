n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 2
for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]       # 마지막 타일의 경우의 수 = 마지막 전 타일의 경우의 수 + 마지막 전전 타일의 경우의 수
print(dp[n] % 10007)