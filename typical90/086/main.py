N, Q = map(int, input().split())
# A_list = list(map(int, input().split()))
MOD = 1000000007

dp = [[True]*2**N for _ in range(60)]

for _ in range(Q):
    x, y, z, w = map(int, input().split())
    x, y, z = x-1, y-1, z-1
    for i in range(60):
        tobe = w >> i & 1
        for j in range(2**N):
            if dp[i][j] == False:
                continue
            if (j >> x & 1) | (j >> y & 1) | (j >> z & 1) != tobe:
                dp[i][j] = False
        
ans = 1
for i in range(60):
    cnt = len([j for j in range(2**N) if dp[i][j]])
    ans *= cnt
    ans %= MOD

print(ans)




