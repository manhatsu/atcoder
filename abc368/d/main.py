from collections import defaultdict, deque
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

N, K = map(int, input().split())
if N == 1:
    ans = 1
else:
    G = [set() for i in range(N)]
    for i in range(N-1):
        a, b = map(int, input().split())
        a, b = a-1, b-1
        G[a].add(b)
        G[b].add(a)
    V = list(map(int, input().split())) # 必要な頂点
    V = set([v-1 for v in V])

    dim = [len(G[v]) for v in range(N)]
    W = [i for i, d in enumerate(dim) if d == 1]
    Q = deque(W)

    ans = N
    while(Q):
        w = Q.popleft()
        if w in V:
            continue
        ans -= 1
        nex = G[w].pop()
        G[nex].discard(w)
        dim[nex] -= 1
        if dim[nex] == 1:
            Q.append(nex)

print(ans)


