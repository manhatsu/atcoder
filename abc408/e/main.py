from collections import defaultdict, deque
import dis
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys

sys.setrecursionlimit(4100000)
import heapq
try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, M = map(int, input().split())
# A = list(map(int, input().split()))

G = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, d = map(int, input().split())
    u, v = u-1, v-1
    G[u].append((v, d))
    G[v].append((u, d))


def is_ok(val): # valからコストを増やさずに到達できるか
    dist = [INF] * N
    dist[0] = 0
    pq = []
    heapq.heappush(pq, (0, 0))  # (コスト, 頂点)
    while len(pq) != 0:
        nd, nv = heapq.heappop(pq)
        if nd > dist[nv]:  # コストが今までより大きい場合スキップ
            continue
        for lv, cost in G[nv]:
            if (dist[nv] | cost) < dist[lv]:  # コストが今までより小さい場合更新
                if (cost & val) == cost:
                    dist[lv] = dist[nv] | cost
                    heapq.heappush(pq, (dist[lv], lv))

    if dist[N-1] == INF:
        return False
    return True



ans = ['1']*30
for i in range(30):
    ans[i] = '0'
    val = int(''.join(ans), 2)
    if is_ok(val):
        continue
    else:
        ans[i] = '1'


print(int(''.join(ans), 2))