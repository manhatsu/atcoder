N, L = map(int, input().split())
# A_list = list(map(int, input().split()))

if N < L:
    ans = 1
else:
    dp = [0]*(N+1)
    for i in range(L):
        dp[i] = 1

    for i in range(L, N+1):
        dp[i] = dp[i-1]+dp[i-L]
        
    ans = dp[N] % (10**9+7)

print(ans)

