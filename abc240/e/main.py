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

N = int(input())
# N, K = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N-1):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    G[u].append(v)
    G[v].append(u)

G[0].append(-1)

# print(G)

L = [-1]*N
R = [-1]*N


num = 1
def dfs(v, p):
    # print('v', v, 'p', p)
    global num
    if len(G[v]) == 1:
        L[v] = num
        R[v] = num
        num += 1
        return
    for lv in G[v]:
        if lv == p:
            continue
        dfs(lv, v)
        if L[v] == -1:
            L[v] = L[lv]
        else:
            L[v] = min(L[v], L[lv])
        if R[v] == -1:
            R[v] = R[lv]
        else:
            R[v] = max(R[v], R[lv])

dfs(0, -1)

for i in range(N):
    print(L[i], R[i])
