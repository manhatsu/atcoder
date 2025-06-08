from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
sys.set_int_max_str_digits(10000000)
sys.setrecursionlimit(4100000)
import heapq
try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, M = map(int, input().split())
# A = list(map(int, input().split()))

L = []
for _ in range(M):
    x, y, z = map(int, input().split())
    x, y = x-1, y-1
    L.append((x, y, z))

ans = [[-1]*N for _ in range(30)]

for i in range(30):
    G = [[] for _ in range(N)]
    for x, y, z in L:
        if (z >> i) & 1:
            G[x].append((y, 1))
            G[y].append((x, 1))
        else:
            G[x].append((y, 0))
            G[y].append((x, 0))
    group_lists = []
    seen = set()
    for j in range(N):
        if j in seen:
            continue
        groups = [set(), set()]
        seen.add(j)
        Q  = deque()
        groups[0].add(j)
        Q.append((j, 0))
        while Q:
            v, _group = Q.popleft()
            for u, w in G[v]:
                if w == 0: # 同じグループ
                    if u in seen:
                        if u in groups[1-_group]:
                            print(-1)
                            sys.exit()
                        continue
                    groups[_group].add(u)
                    seen.add(u)
                    Q.append((u, _group))
                else:
                    if u in seen:
                        if u in groups[_group]:
                            print(-1)
                            sys.exit()
                        continue
                    groups[1-_group].add(u)
                    seen.add(u)
                    Q.append((u, 1-_group))
        if len(groups[0]) < len(groups[1]):
            groups[0], groups[1] = groups[1], groups[0]
        group_lists.append(groups)

    for group0, group1 in group_lists:
        for v in group0:
            ans[i][v] = 0
        for v in group1:
            ans[i][v] = 1

ret = [0]*N
for i in range(30):
    for j in range(N):
        ret[j] |= (ans[i][j] << i)

print(*ret)