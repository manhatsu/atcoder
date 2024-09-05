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

F = [[0]*N for i in range(N)]
F[N//2][N//2] = 'T'

num = 1
phase = 0
dw = [1, 0, -1, 0]
dh = [0, 1, 0, -1]
nh = 0
nw = 0

iter = 0
while (num < N*N):
    if nh < 0 or nh >= N or nw < 0 or nw >= N:
        nh -= dh[phase]
        nw -= dw[phase]
        phase = (phase+1)%4
        nh += dh[phase]
        nw += dw[phase]
        continue
    if F[nh][nw] != 0:
        nh -= dh[phase]
        nw -= dw[phase]
        phase = (phase+1)%4
        nh += dh[phase]
        nw += dw[phase]
        continue
    F[nh][nw] = num
    num += 1
    nh += dh[phase]
    nw += dw[phase]

for i in range(N):
    print(*F[i])
