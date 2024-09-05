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

N = int(input())

A = [[] for i in range(N)]

for i in range(N):
    for j in range(N):
        Aij = list(map(int, input().split()))
        A[i].append(Aij)

S = [[[0]*(N+1) for j in range(N+1)] for i in range(N+1)] # index0は番兵

for i in range(0, N):
    for j in range(0, N):
        for k in range(0, N):
            S[i+1][j+1][k+1] = S[i][j+1][k+1]+S[i+1][j][k+1]-S[i][j][k+1] \
            + S[i+1][j+1][k] - S[i][j+1][k] - S[i+1][j][k] + S[i][j][k] + A[i][j][k] # Aは0indexed

# print(S)

Q = int(input())
for _ in range(Q):
    lx, rx, ly, ry, lz, rz = map(int, input().split())
    sigma = S[rx][ry][rz] - S[rx][ry][lz-1] - (S[rx][ly-1][rz] - S[rx][ly-1][lz-1]) \
        - (S[lx-1][ry][rz] - S[lx-1][ry][lz-1] - (S[lx-1][ly-1][rz] - S[lx-1][ly-1][lz-1]))
    print(sigma)