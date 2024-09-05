# ワーシャルフロイド法のテンプレ
N = 2 #　要素数

# d: 自身との距離0, それ以外の距離無限で初期化する
INF = float("inf")
d = [[INF]*N for i in range(N)]
for i in range(N):
    d[i][i] = 0

# ------
# inputを使ってより小さい値で更新しておく
# for _ in range(num_of_inputs):
#   u, v, c = map(int, input().split())
#   u, v = u-1, v-1
#   d[u][v] = min(d[u][v], c)
#   d[v][u] = min(d[v][u], c)
# ------

# 最短距離更新
for k in range(N): # 経由する点
    for i in range(N): # 始点
        for j in range(N): # 終点
            d[i][j] = min(d[i][k]+d[k][j], d[i][j])

