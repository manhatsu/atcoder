N = int(input())
# N, K = map(int, input().split())

INF = float("inf")

C = [0]*(N+1)
Z = [0]*(N+1)
sigmaz = 0
for i in range(N):
    x, y, z = map(int, input().split())
    if x > y:
        C[i+1] = 0
    else:
        C[i+1] = (y-x)//2+1
    Z[i+1] = z
    sigmaz += z

dp = [[INF]*(sigmaz+1) for i in range(N+1)]
for i in range(N+1):
    dp[i][0] = 0

for i in range(1, N+1):
    for w in range(sigmaz+1):
        dp[i][w] = dp[i - 1][w]
        if w >= Z[i]:
            dp[i][w] = min(dp[i][w], dp[i - 1][w - Z[i]] + C[i])

print(min(dp[N][sigmaz//2+1:]))




