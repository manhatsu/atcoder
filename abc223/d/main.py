from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
import heapq
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, M = map(int, input().split())

G = [[] for i in range(N)]
into_num = [0]*N
for i in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    G[a].append(b)
    into_num[b] += 1

Q = [i for i in range(N) if into_num[i] == 0]

heapq.heapify(Q)

ans = []
while Q:
    q = heapq.heappop(Q)
    ans.append(q)
    for lq in G[q]:
        into_num[lq] -= 1
        if into_num[lq] == 0:
            heapq.heappush(Q, lq)

if len(ans) == N:
    ans = [i+1 for i in ans]
    print(*ans)
else:
    print(-1)


