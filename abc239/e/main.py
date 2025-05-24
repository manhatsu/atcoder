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

N, Q = map(int, input().split())
X = list(map(int, input().split()))

G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

L = dict()

def dfs(v, pv):
    M = SortedList()
    for lv in G[v]:
        if lv == pv:
            continue
        M.update(dfs(lv, v))
        M = SortedList(M[-20:])
    M.add(X[v])
    M = SortedList(M[-20:])
    L[v] = M
    return M

dfs(0, -1)
# print(L)


for _ in range(Q):
    v, k = map(int, input().split())
    v -= 1
    print(L[v][-k])