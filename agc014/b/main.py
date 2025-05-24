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
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    G[a].append(b)
    G[b].append(a)

for g in G:
    if len(g) % 2:
        print("NO")
        exit()

print("YES")