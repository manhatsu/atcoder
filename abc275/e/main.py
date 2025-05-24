MOD = 998244353
N, M, K = map(int, input().split())
# A_list = list(map(int, input().split()))

dp = [0]*(N+1)

dp[0] = 1

ans = 0

for _ in range(K):
    new_dp = [0]*(N+1)
    for x in range(N):
        for m in range(1, M+1):
            dst = x+m
            if dst > N:
                dst = N - (dst-N)
            new_dp[dst] += dp[x] * pow(M, -1, MOD) % MOD
            new_dp[dst] %= MOD
    ans += new_dp[N]
    ans %= MOD
    dp = new_dp

print(ans)
                





