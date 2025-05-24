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

N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

Z = []
P = []
for i in range(N):
    x, y, p = map(int, input().split())
    Z.append((x, y))
    P.append(p)

dist = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        dist[i][j] = abs(Z[i][0] - Z[j][0]) + abs(Z[i][1] - Z[j][1])


def is_ok(s):
    G = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if dist[i][j] <= s*P[i]:
                G[i].append(j)
    
    ret = False
    for i in range(N):
        seen = [0]*N
        seen[i] = 1
        Q = deque([i])
        while Q:
            v = Q.popleft()
            for lv in G[v]:
                if seen[lv]:
                    continue
                seen[lv] = 1
                Q.append(lv)
        if sum(seen) == N:
            ret = True
            break
    return ret

def bs(ok, ng):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(bs(10**10, 0))