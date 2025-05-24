N = int(input())
A = list(map(int, input().split()))
MOD = 998244353

if N == 1:
    print(1)
else:
    dp = [[[0]*(N+1) for i in range(N+1)] for j in range(N+1)]

    for i in range(1, N):
        for j in range(i+1, N+1):
            dp[2][i][j] = 1

    for k in range(3, N+1):
        for i in range(1, N-1):
            for j in range(i+1, N):
                for t in range(j+1, N+1):
                    if A[j-1]-A[i-1] == A[t-1]-A[j-1]:
                        dp[k][j][t] = (dp[k][j][t]+dp[k-1][i][j])%MOD

    R = [N]         
    for k in range(2, N+1):
        ret = 0
        for i in range(1, N+1):
            for j in range(1, N+1):
                ret = (ret + dp[k][i][j])%MOD
        R.append(ret%MOD)

    print(*R)