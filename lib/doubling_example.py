# abc367e
# O(log(K)*要素数N)
X = [5, 2, 6, 3, 1, 4, 6]
X = [x-1 for x in X]

N = len(X)
K = 10**18 # < 2**60

dv = [[-1]*N for i in range(61)] # range(math.log2(K)+1)まで考慮すれば良い

for j in range(N):
    dv[0][j] = X[j] # 2**0 = 1回目の値で初期化

for i in range(1, 61):
    for j in range(N):
        dv[i][j] = dv[i-1][dv[i-1][j]]

now = [j for j in range(N)]
for i in range(61):
    if K >> i & 1:
        for j in range(N):
            now[j] = dv[i][now[j]]