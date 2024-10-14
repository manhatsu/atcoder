# from collections import defaultdict, deque
from itertools import combinations, permutations
# import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N = int(input())
MG = int(input())

G = [[0]*N for i in range(N)]
H = [[0]*N for i in range(N)]
C = [[0]*N for i in range(N)]

for i in range(MG):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    G[u][v] = 1
    G[v][u] = 1

MH = int(input())

for i in range(MH):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    H[u][v] = 1
    H[v][u] = 1

for i in range(N-1):
    A = list(map(int, input().split()))
    for j in range(i+1, N):
        C[i][j] = A[j-(i+1)]

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if C[i][j] == 0:
            C[i][j] = C[j][i]

# print(C)

T = [i for i in range(N)]
P = list(permutations(T))

ans = float('inf')
for p in P:
    temp = 0
    for i in range(N):
        for j in range(N):
            if H[i][j] != G[p[i]][p[j]]:
                temp += C[i][j]
                # H[i][j] = 1 - H[i][j]
                # H[j][i] = 1 - H[j][i]
                # G[p[i]][p[j]] = 1 - G[p[i]][p[j]]
                # G[p[j]][p[i]] = 1 - G[p[j]][p[i]]
    ans = min(ans, temp)

print(ans//2)

                



