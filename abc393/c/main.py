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
# A = list(map(int, input().split()))

G = [set() for _ in range(N)]

ans = 0
if M == 0:
    ans = 0
else:
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        if a == b:
            ans += 1
            continue
        if a in G[b] or b in G[a]:
            ans += 1
            continue
        G[a].add(b)
        G[b].add(a)

print(ans)