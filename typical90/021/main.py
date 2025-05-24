from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from multiprocessing.connection import answer_challenge
from re import S
from sortedcontainers import SortedSet, SortedDict, SortedList
from atcoder.scc import SCCGraph
import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, M = map(int, input().split())

G = SCCGraph(N)


for _ in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    G.add_edge(a, b)

L = G.scc()

ans = 0
for l in L:
    ans += len(l) * (len(l)-1) // 2

print(ans)

