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
C = list(map(int, input().split()))

S = [set([c]) for c in C]
D = {i:i for i in range(N)}

for _ in range(Q):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    if len(S[D[a]]) > len(S[D[b]]):
        D[a], D[b] = D[b], D[a]
    S[D[b]] |= S[D[a]]
    S[D[a]] = set()
    print(len(S[D[b]]))