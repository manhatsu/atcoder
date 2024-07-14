from collections import deque

N = int(input()) # 頂点数

G = [[] for _ in range(N)] # 隣接グラフ

inf = 10**9
dist = [inf]*N

# 開始点
dist[0] = 0
Q = deque([0])

while Q:
    v = Q.popleft()
    for lv in G[v]:
        if dist[lv] > dist[v]+1:
            dist[lv] = dist[v]+1
            Q.append(lv)

# 2次元グリッド
W, H = map(int, input().split())
dist = [[inf]*W for _ in range(H)]
F = [] # field

dh = [0, 1, 0, -1]
dw = [1, 0, -1, 0]

sh, sw = 0, 0 # 始点
dist[sh][sw] = 0

Q = deque()
Q.append((sh, sw))

while Q:
    nh, nw = Q.popleft()
    for i in range(4):
        ph, pw = nh+dh[i], nw+dw[i]
        if 0>ph or ph>=H or 0>pw or pw>=W:
            continue
        if F[ph][pw] == '#':
            continue
        if dist[ph][pw] > dist[nh][nw]+1:
            dist[ph][pw] = dist[nh][nw]+1
            Q.append((ph, pw))




