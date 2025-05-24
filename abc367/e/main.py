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

N, K = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))

X = [x-1 for x in X]

dv = [[-1]*N for i in range(61)]

for j in range(N):
    dv[0][j] = X[j]

for i in range(1, 61):
    for j in range(N):
        dv[i][j] = dv[i-1][dv[i-1][j]]

now = [j for j in range(N)]
for i in range(61):
    if K >> i & 1:
        for j in range(N):
            now[j] = dv[i][now[j]]

ans = []
for j in range(N):
    ans.append(A[now[j]])

print(*ans)