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


def solve(N, C, G):
    seen = [[-1]*N for _ in range(N)]
    seen[0][N-1] = 0
    Q = deque()
    Q.append((0, N-1, 0))
    while Q:
        x, y, d = Q.popleft()
        for nx in G[x]:
            for ny in G[y]:
                if seen[nx][ny] != -1:
                    continue
                if C[nx] == C[ny]:
                    continue
                seen[nx][ny] = d + 1
                Q.append((nx, ny, d + 1))
    print(seen[N-1][0])


T = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))
for _ in range(T):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u, v = u-1, v-1
        G[u].append(v)
        G[v].append(u)
    solve(N, C, G)