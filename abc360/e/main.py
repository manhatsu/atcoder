N, K = map(int, input().split())
MOD = 998244353

# 1番左にいる確率pだけ求めれば，それ以外の場所の確率は(1-p)/(N-1)で求まるので計算不要
'''
dp = [0]*(K+1)
dp[0] = 1
a = (N**2-2*N)%MOD*pow(N, -2, MOD)
b = 2*pow(N, -2, MOD)
for k in range(1, K+1):
    dp[k] = (dp[k-1]*a+b)%MOD

if N == 1:
    ans = 1
else:
    ans = dp[K] + (1-dp[K])*pow(N-1, -1, MOD)*(N+2)*(N-1)//2

print(ans%MOD)
'''
# DPをO(K)で回すとTLE,ではなく，最後のNでTLEしてる
dp = [[0]*2 for i in range(K+1)]

dp[0][0] = 1
dp[0][1] = 0

MM = (N**2%MOD-2*N+2)%MOD
NN = pow(N, -2, MOD)

for k in range(1, K+1):
    dp[k][0] = (dp[k-1][0]*MM%MOD*NN%MOD + (N-1)*dp[k-1][1]%MOD*2*NN%MOD)%MOD
    dp[k][1] = (dp[k-1][1]*MM%MOD*NN%MOD + (dp[k-1][0]+(N-2)*dp[k-1][1])%MOD*2*NN%MOD)%MOD


ans = dp[k][0] + dp[k][1]*(N+2)*(N-1)//2

print(ans%MOD)
'''
a = (-2*N+2)*pow(N, -2, MOD)%MOD
p = (N**2-2*N)*pow(N, -2, MOD)%MOD

P0 = (1+a*pow(1-p, K, MOD)*pow(1-p, -1, MOD))%MOD
ans = P0
for i in range(2, N+1):
    ans += i*(1-P0)*pow(N-1, -1, MOD)%MOD

print(ans%MOD)
'''




