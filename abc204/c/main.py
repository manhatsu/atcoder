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

G = [[] for i in range(N)]

if M > 0:
    for i in range(M):
        a, b = map(int, input().split())
        a, b = a-1, b-1
        G[a].append(b)

ans = 0
for i in range(N):
    seen = [0]*N
    seen[i] = 1
    ans += 1
    Q = deque()
    Q.append(i)
    while Q:
        q = Q.popleft()
        for lq in G[q]:
            if seen[lq]:
                continue
            seen[lq] = 1
            ans += 1
            Q.append(lq)

print(ans)
    