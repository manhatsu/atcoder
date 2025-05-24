from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
from atcoder.scc import SCCGraph
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N = int(input())
# N, K = map(int, input().split())
X = list(map(int, input().split()))
X = [x-1 for x in X]
C = list(map(int, input().split()))

G = SCCGraph(N)
for i, x in enumerate(X):
    G.add_edge(i, x)

L = G.scc()
# print(L)

ans = 0
for M in L:
    if len(M) == 1:
        continue
    temp = INF
    for m in M:
        temp = min(temp, C[m])
    ans += temp

print(ans)