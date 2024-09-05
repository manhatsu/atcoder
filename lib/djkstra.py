# djkstra
# 計算量はO((V+E)log(V)) V: 頂点の数、E: 辺の数
# 有向グラフでも無向グラフでも使える
# 全ての辺のコストが正である必要あり。

import heapq

N, M = map(int, input().split()) # 頂点数，辺の数

G = [[] for _ in range(N)]
for i in range(M) :
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append((b, c)) # 隣接頂点, コスト
    G[b].append((a, c))


inf = int(1e18)
dist = [inf]*N

# 0スタート
dist[0] = 0
pq = []
heapq.heappush(pq, (0, 0)) # pqに(コスト，頂点)を追加する コストでソートしたいのでタプルの先頭に入れる

while len(pq) != 0:
    ncost, nv = heapq.heappop(pq)
    if ncost > dist[nv]: # コストが今までより大きい場合スキップ
        continue
    for lv, cost in G[nv]:
        if dist[lv] > dist[nv]+cost:
            dist[lv] = dist[nv]+cost
            heapq.heappush(pq, (dist[lv], lv))


