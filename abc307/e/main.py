MOD = 998244353
N, M = map(int, input().split())
# A_list = list(map(int, input().split()))

dp = [[0]*2 for _ in range(N)]

dp[0][0] = 0
dp[0][1] = M

for i in range(1, N):
    dp[i][1] = dp[i-1][0]
    dp[i][0] = dp[i-1][1]*(M-1)%MOD + dp[i-1][0]*(M-2)%MOD
    dp[i][0] %= MOD

print(dp[N-1][0] % MOD)


