MOD = 998244353

N, A, B, P, Q = map(int, input().split())
# A_list = list(map(int, input().split()))

dpt = [0]*(N+1)
dpa = [0]*(N+1)

dpt[A] = 1
dpa[B] = 1

ans = 0
for t in range(N): # (min(N-A, N-B)):
    new_dpt = [0]*(N+1)
    new_dpa = [0]*(N+1)
    for x in range(N):
        for i in range(1, P+1):
            new_dpt[min(N, x+i)] += dpt[x] * pow(P, -1, MOD) % MOD
            new_dpt[min(N, x+i)] %= MOD
        for i in range(1, Q+1):
            new_dpa[min(N, x+i)] += dpa[x] * pow(Q, -1, MOD) % MOD
            new_dpa[min(N, x+i)] %= MOD
    ans += new_dpt[N]*sum(dpa[:N])%MOD
    ans %= MOD
    dpt = new_dpt
    dpa = new_dpa

print(ans)