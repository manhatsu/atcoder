from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from re import S
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

F = [[] for i in range(N)]
G = [[] for i in range(N)]
into_num = [0]*N

for i in range(N):
    L = list(map(int, input().split()))
    if len(L) == 1:
        continue
    L = L[1:]
    for l in L:
        l -= 1
        F[i].append(l)
        into_num[i] += 1
        G[l].append(i)

seen = [0]*N
Q = deque()
seen[0] = 1
Q.append(0)

while Q:
    q = Q.popleft()
    for lq in F[q]:
        if seen[lq]:
            continue
        seen[lq] = 1
        Q.append(lq)

T = [i for i in range(N) if into_num[i] == 0]
Q = deque(T)
while Q:
    q = Q.popleft()
    for lq in G[q]:
        into_num[lq] -= 1
        if into_num[lq] == 0:
            T.append(lq)
            Q.append(lq)

ans = [t+1 for t in T if seen[t] == 1 and t != 0]

print(*ans)