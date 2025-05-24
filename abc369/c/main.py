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
# N, K = map(int, input().split())
A = list(map(int, input().split()))

L = []
ans = N
prev_diff = INF
j = 0
while j < N-1:
    start = j
    diff = A[j+1] - A[j]
    while True:
        j += 1
        if j >= N-1:
            break
        if A[j+1] - A[j] != diff:
            break
    L.append((start, j))

# print(ans)
# print(L)

for s, e in L:
    ans += (e-s+1)*(e-s) // 2

print(ans)