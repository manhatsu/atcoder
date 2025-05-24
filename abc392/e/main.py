from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
from atcoder.dsu import DSU
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, M = map(int, input().split())

amari_nodes = []

U = DSU(N)
for i in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    if not U.same(a, b):
        U.merge(a, b)
    else:
        amari_nodes.append((a, b, i))

P = []
rem_nodes = [[] for _ in range(N)]
for g in U.groups():
    parent = U.leader(g[0])
    P.append(parent)

ans = []
if len(amari_nodes) > 0:
    for a, b, i in amari_nodes:
        parent = U.leader(a)
        rem_nodes[parent].append((a, b, i))

    P = [(len(rem_nodes[i]), i) for i in P]
    P = SortedList(P)

    while len(P) > 1:
        _, p0 = P.pop(0)
        _, p1 = P.pop()
        a, b, i = rem_nodes[p1].pop()
        ans.append((i+1, a+1, p0+1))
        rem_nodes[p1] += rem_nodes[p0]
        P.add((len(rem_nodes[p1]), p1))

print(len(ans))
if len(ans) > 0:
    for a, b, i in ans:
        print(a, b, i)
