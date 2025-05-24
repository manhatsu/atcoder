# from collections import defaultdict, deque
# from itertools import combinations, permutations
# import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, M = map(int, input().split())

G = [[] for i in range(N)]

if M > 0:
    for i in range(M):
        u, v = map(int, input().split())
        u, v = u-1, v-1
        G[u].append(v)
        G[v].append(u)

group = [-1]*N

j = 0
for i in range(N):
    if group[i] != -1:
        continue
    group[i] = j
    
    Q = deque([i])
    while Q:
        q = Q.popleft()
        if len(G[q]) == 0:
            continue
        for lq in G[q]:
            if group[lq] != -1:
                continue
            group[lq] = j
            Q.append(lq)
    
    j += 1

# print(*group)

NGs = set()
K = int(input())
for i in range(K):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    gx = group[x]
    gy = group[y]
    if gx > gy:
        temp = gx
        gx = gy
        gy = temp
    NGs.add((gx, gy))

# print(*NGs)

Q = int(input())
for i in range(Q):
    p, q = map(int, input().split())
    p, q = p-1, q-1
    gp = group[p]
    gq = group[q]
    if gp > gq:
        temp = gp
        gp = gq
        gq = temp
    if (gp, gq) in NGs:
        print('No')
    else:
        print('Yes')

    


