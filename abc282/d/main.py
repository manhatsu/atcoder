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

is2G = True
ret = N*(N-1)//2-M
G = [[] for i in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    G[u].append(v)
    G[v].append(u)

seen = [-1]*N
for i in range(N):
    if seen[i] != -1:
        continue
    count = [0]*2
    seen[i] = 0
    count[0] += 1
    Q = deque()
    Q.append(i)
    while Q:
        q = Q.popleft()
        for lq in G[q]:
            if seen[lq] != -1:
                if seen[lq] == seen[q]:
                    is2G = False
                    break
                continue
            seen[lq] = 1 - seen[q]
            count[seen[lq]] += 1
            Q.append(lq)
        if not is2G:
            break
    if not is2G:
        break
    if count[0] > 1:
        ret -= count[0]*(count[0]-1) // 2
    if count[1] > 1:
        ret -= count[1]*(count[1]-1) // 2

if not is2G:
    ret = 0

print(ret)




