from collections import defaultdict, deque
from contextlib import AsyncExitStack
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

N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

G = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

ans = 0

def dfs(v, pv):
    
    global ans

    cand_p = []
    for lv in G[v]:
        if lv == pv:
            continue
        cand_p.append(dfs(lv, v))

    sorted_cand_p = sorted(cand_p)

    if len(sorted_cand_p) >= 3:
        p = sum(sorted_cand_p[-3:]) + 1
    else:
        p = 1
    
    # dfsのループの中でmaxを更新しないと、隣接する枝を選ぶときに重複が発生してしまう
    if len(sorted_cand_p) >= 4:
        ans = max(ans, sum(sorted_cand_p[-4:]) + 1)
    if len(sorted_cand_p) > 0:
        ans = max(ans, sorted_cand_p[-1] + 1)

    return p

dfs(0, -1)

print(ans if ans >= 5 else -1)
