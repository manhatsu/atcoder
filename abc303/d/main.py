
X, Y, Z = map(int, input().split())
S = input()
# A_list = list(map(int, input().split()))

INF = float('inf')

dp = [[0]*2 for i in range(len(S)+1)] # 0:ON, 1: OFF
dp[0][0] = Z

for i in range(1, len(S)+1):
    if S[i-1] == 'A':
        dp[i][0] = min(dp[i-1][0]+X, dp[i-1][1]+Z+X)
        dp[i][1] = min(dp[i-1][0]+Z+Y, dp[i-1][1]+Y)
    else:
        dp[i][0] = min(dp[i-1][0]+Y, dp[i-1][1]+Z+Y)
        dp[i][1] = min(dp[i-1][0]+Z+X, dp[i-1][1]+X)

print(min(dp[len(S)][0], dp[len(S)][1]))



