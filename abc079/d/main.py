from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

# N = int(input())
H, W = map(int, input().split())
 #A = list(map(int, input().split()))

INF = float("inf")
d = []
for i in range(10):
    d.append(list(map(int, input().split())))

# 最短距離更新
for k in range(10): # 経由する点
    for i in range(10): # 始点
        for j in range(10): # 終点
            if d[i][k] == INF or d[k][j] == INF: # オーバーフロー対策
                continue
            d[i][j] = min(d[i][k]+d[k][j], d[i][j])

F = []
for i in range(H):
    F.append(list(map(int, input().split())))

ans = 0
for h in range(H):
    for w in range(W):
        if F[h][w] == -1:
            continue
        ans += d[F[h][w]][1]

print(ans)

