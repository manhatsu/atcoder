from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
# sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")
# from icecream import # ic

N, M = map(int, input().split())
# A = list(map(int, input().split()))

G = [[] for _ in range(N)]

if M > 0:
    for _ in range(M):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)

A = [[0]*4 for _ in range(N)]
for i in range(N):
    A[i][0] = i+1

for i in range(N):
    seen = [0]*N
    Q = deque()
    seen[i] = 1
    Q.append((i, 0))
    while Q:
        v, d = Q.popleft()
        for lv in G[v]:
            if seen[lv]:
                continue
            seen[lv] = 1
            A[i][d+1] += lv+1
            if d+1 == 3:
                continue
            Q.append((lv, d+1))

for i in range(N):
    for j in range(1, 4):
        A[i][j] += A[i][j-1]

# ic(A)

R = int(input())

for _ in range(R):
    x, k = map(int, input().split())
    print(A[x-1][k])
