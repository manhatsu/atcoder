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

N, M = map(int, input().split())
G = [[] for _ in range(N)]

if M == 0:
    print(1)
    exit()

for _ in range(M):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    G[u].append(v)
    G[v].append(u)

K = 0
seen = [0]*N
def dfs(v):
    global K
    if K >= 10**6:
        return
    K += 1
    seen[v] = 1
    for lv in G[v]:
        if seen[lv]:
            continue
        dfs(lv)
    seen[v] = 0

dfs(0)
print(K if K < 10**6 else 10**6)
    
