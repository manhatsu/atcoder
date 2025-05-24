from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from operator import not_
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys

sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

from atcoder.dsu import DSU

N, M = map(int, input().split())
# A = list(map(int, input().split()))
G = [[] for _ in range(N)]
H = [[] for _ in range(N)]
if M > 0:
    for _ in range(M):
        u, v = map(int, input().split())
        u, v = u-1, v-1
        G[u].append(v)
        H[v].append(u)

T = DSU(N)
U = DSU(N)

for i in range(N):
    for j in G[i]:
        T.merge(i, j)
    for j in H[i]:
        U.merge(i, j)
    if U.size(i) != i+1:
        print(-1)
    else:
        print(T.size(i)-U.size(i))