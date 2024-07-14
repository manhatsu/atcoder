
N = int(input())
S = input()
T = "atcoder"

dp = [[0]*(len(T)+1) for _ in range(N+1)]
for i in range(N+1):
    dp[i][0] = 1
    dp[0][0] = 1

for i in range(1, N+1):
    for j in range(1, len(T)+1):
        if S[i-1] == T[j-1]:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1] % (10**9+7))




