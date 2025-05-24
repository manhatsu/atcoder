N = int(input())
# N, K = map(int, input().split())
A = list(map(int, input().split()))

S = []
for i in range(N):
    S.append(input())

INF = float("inf")
d = [[INF]*N for i in range(N)]
val = [[0]*N for i in range(N)]
for i in range(N):
    d[i][i] = 0
    for j in range(N):
        val[i][j] = A[i]

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if S[i][j] == 'Y':
            d[i][j] = 1
            val[i][j] += A[j]

# 最短距離更新
for k in range(N): # 経由する点
    for i in range(N): # 始点
        for j in range(N): # 終点
            if d[i][k] == INF or d[k][j] == INF:
                continue
            if d[i][j] > d[i][k]+d[k][j]:
                d[i][j] = d[i][k]+d[k][j]
                val[i][j] = val[i][k]+val[k][j]-A[k]
            elif d[i][j] == d[i][k]+d[k][j]:
                val[i][j] = max(val[i][j], val[i][k]+val[k][j]-A[k])

Q = int(input())
for _ in range(Q):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    if d[u][v] == INF:
        print('Impossible')
    else:
        print(d[u][v], val[u][v])
