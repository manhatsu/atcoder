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

N, X, Y = map(int, input().split())
A = sorted(list(map(int, input().split())))[::-1]
B = sorted(list(map(int, input().split())))[::-1]

x, y = 0, 0
for i in range(N):
    x += A[i]
    y += B[i]
    if x > X or y > Y:
        break

print(i+1)