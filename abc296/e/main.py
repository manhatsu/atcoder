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
A = list(map(int, input().split()))

G = SCCGraph(N)

ans = 0

for i, a in enumerate(A):
    if i == a-1:
        ans += 1
    G.add_edge(i, a-1)

cycles = G.scc()

for c in cycles:
    if len(c) >= 2:
        ans += len(c)

print(ans)

