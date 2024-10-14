MOD = 998244353
S = input()
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))

dp = [[0]*(len(S)+1) for _ in range(len(S)+1)]
dp[0][0] = 1

for i in range(1, len(S)+1):
    if S[i-1] == '(':
        for j in range(len(S)+1):
            dp[i][j] += dp[i-1][j-1]%MOD
    elif S[i-1] == ')':
        for j in range(len(S)+1):
            if j >= (i-j):
                dp[i][j] += dp[i-1][j]%MOD
            # else:
                # dp[i][j] = 0
    else:
        for j in range(len(S)+1):
            dp[i][j] += dp[i-1][j-1]%MOD
            if j >= (i-j):
                dp[i][j] += dp[i-1][j]%MOD
    dp[i][j] = dp[i][j]%MOD

# for i in range(len(S)+1):
    # print(*dp[i])

ans = 0
if len(S)%2 == 0:
    ans = dp[len(S)][len(S)//2]%MOD

print(ans)



