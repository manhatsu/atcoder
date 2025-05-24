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
# from icecream import ic

N, M = map(int, input().split())

G = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    G[u].append(v)
    G[v].append(u)

kakutei_kuro = set()
kakutei_shiro = set()

doreka_kuros = []

def F(p, d):
    dist = [-1]*N
    Q = deque()
    Q.append(p)
    dist[p] = 0
    dist_is_ds = set()
    if d == 0:
        if p in kakutei_shiro:
            return False
        kakutei_kuro.add(p)
        return True
    else:
        if p in kakutei_kuro:
            return False
        kakutei_shiro.add(p)
    while Q:
        q = Q.popleft()
        for lq in G[q]:
            if dist[lq] == -1:
                dist[lq] = dist[q]+1
                if dist[lq] < d:
                    if lq in kakutei_kuro:
                        return False
                    kakutei_shiro.add(lq)
                    Q.append(lq)
                elif dist[lq] == d:
                    dist_is_ds.add(lq)
    
    # ic(dist_is_ds)

    if len(dist_is_ds) == 0:
        return False
    elif len(dist_is_ds) == 1:
        kakutei_kuro.add(dist_is_ds.pop())
        return True
    else:
        doreka_kuros.append(dist_is_ds)
        return True
    
K = int(input())
for _ in range(K):
    p, d = map(int, input().split())
    p -= 1
    ret = F(p, d)
    if not ret:
        print("No")
        exit()

# ic(doreka_kuros)
# ic(kakutei_kuro)
# ic(kakutei_shiro)

ret = [1]*N
for s in kakutei_shiro:
    ret[s] = 0

if sum(ret) == 0:
    print("No")
    exit()

for dk in doreka_kuros:
    if kakutei_shiro & dk == dk:
        print("No")
        exit()


print("Yes")
print(''.join(map(str, ret)))

    