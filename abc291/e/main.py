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
in_num = [0]*N
for i in range(M):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    G[x].append(y)
    in_num[y] += 1

count = 0
ret = True
Q = deque()
for i in range(N):
    if in_num[i] == 0:
        Q.append(i)

ans = []
while Q:
    if len(Q) > 1:
        ret = False
        break
    q = Q.popleft()
    ans.append(q)
    for lq in G[q]:
        in_num[lq] -= 1
        if in_num[lq] == 0:
            Q.append(lq)

if ret and len(ans) == N:
    print('Yes')
    ret = [0]*N
    for i, q in enumerate(ans):
        ret[q] = i+1
    print(*ret)
else:
    print('No')



        



