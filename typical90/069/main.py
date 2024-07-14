N, K = map(int, input().split())
# A_list = list(map(int, input().split()))

MOD = 10**9+7

loop = True
if N == 1:
    loop = False
    ret = K
elif N == 2:
    loop = False
    if K < 2:
        ret = 0
    else:
        ret = K*(K-1)
else:
    if K < 3:
        loop = False
        ret = 0
    else:
        ret = K*(K-1)*pow(K-2, N-2, MOD)
        # forloopで掛けるとTLE. powで書けば通る
    
print(ret % MOD)

# 数の大きいMODはpowで計算！（繰り返し二乗法によりO(LogN)で解ける）