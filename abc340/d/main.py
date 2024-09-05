# from collections import defaultdict, deque
# from itertools import combinations, permutations
# import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N = int(input())

import heapq

G = [[] for _ in range(N)]
for i in range(N-1) :
    a, b, j = map(int, input().split())
    j -= 1
    G[i].append((i+1, a)) # 隣接頂点, コスト
    G[i].append((j, b))

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

print(dist[N-1])


