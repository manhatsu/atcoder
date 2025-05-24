H, W, N = map(int, input().split())
# A_list = list(map(int, input().split()))

F = [[0]*W for _ in range(H)]

if N > 0:
    for _ in range(N):
        a, b = map(int, input().split())
        a, b = a-1, b-1
        F[a][b] = 1

dp = [[0]*W for _ in range(H)]

for h in range(H):
    dp[h][0] = 1 - F[h][0]

for w in range(W):
    dp[0][w] = 1 - F[0][w]

for h in range(1, H):
    for w in range(1, W):
        if F[h][w] == 1:
            dp[h][w] = 0
        else:
            dp[h][w] = min(dp[h-1][w], dp[h][w-1], dp[h-1][w-1]) + 1

ans = 0
for h in range(H):
    for w in range(W):
        ans += dp[h][w]

print(ans)



