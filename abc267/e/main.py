from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from multiprocessing import heap
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
import heapq
# from icecream import ic
import copy
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, M = map(int, input().split())
A = list(map(int, input().split()))

G = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    G[u].append(v)
    G[v].append(u)

C = [0]*N
for v in range(N):
    for lv in G[v]:
        C[v] += A[lv]

def is_ok(X, C):
    D = copy.deepcopy(C)
    # D = C.copy()
    Q = deque()
    deleted = [0]*N
    for v in range(N):
        if D[v] <= X:
            Q.append(v)
            deleted[v] = 1
    while Q:
        v = Q.popleft()
        for lv in G[v]:
            if deleted[lv]:
                continue
            D[lv] -= A[v]
            if D[lv] <= X:
                Q.append(lv)
                deleted[lv] = 1
    return all(deleted)

def bs(ok, ng): # okの初期値は-1, ngの初期値は最大idx+1
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        if is_ok(mid, C):
            ok = mid
        else:
            ng = mid
    return ok

print(bs(sum(A), -1))
