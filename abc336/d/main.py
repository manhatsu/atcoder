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
A = list(map(int, input().split()))

i, j = 0, N-1
L = [0]*N
R = [0]*N
ln, rn = 0, 0
for i in range(N):
    if A[i] >= ln+1:
        ln += 1
    else:
        ln = A[i] # 1ではなくA[i]
    L[i] = ln
for j in range(N-1, -1, -1):
    if A[j] >= rn+1:
        rn += 1
    else:
        rn = A[j]
    R[j] = rn

print(max([min(l, r) for l, r in zip(L, R)]))     