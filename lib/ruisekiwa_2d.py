# 2D累積和

N = 5000

F = [[0]*(N+1) for _ in range(N+1)] # 元の配列
# Fに値を入れる
# 0行/列目は番兵

S = [[0]*(N+1) for _ in range(N+1)] # 累積和の配列
for i in range(1, N+1):
    for j in range(1, N+1):
        S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + F[i][j]