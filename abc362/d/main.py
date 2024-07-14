# N = int(input())
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))

import heapq

N, M = map(int, input().split()) # 頂点数，辺の数
A = list(map(int, input().split()))

G = [[] for _ in range(N)]
for i in range(M) :
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append((b, c+A[b])) # 隣接頂点, コスト
    G[b].append((a, c+A[a]))


inf = int(1e18)
dist = [inf]*N

# 0スタート
dist[0] = A[0]
pq = []
heapq.heappush(pq, (A[0], 0)) # pqに(コスト，頂点)を追加する コストでソートしたいのでタプルの先頭に入れる

while len(pq) != 0:
    ncost, nv = heapq.heappop(pq)
    if ncost > dist[nv]: # コストが今までより大きい場合スキップ
        continue
    for lv, cost in G[nv]:
        if dist[lv] > dist[nv]+cost:
            dist[lv] = dist[nv]+cost
            heapq.heappush(pq, (dist[lv], lv))

print(*dist[1:])




