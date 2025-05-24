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
# from icecream import # ic

N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

last_ng_idx = -1
x_idx = -1
y_idx = -1
ans = 0

for i in range(N):
    if A[i] > X or A[i] < Y:
        last_ng_idx = i
        x_idx = -1
        y_idx = -1
        continue
    if A[i] == X:
        x_idx = i
    if A[i] == Y:
        y_idx = i
    # ic(x_idx, y_idx, last_ng_idx)
    if x_idx != -1 and y_idx != -1:
        ans += min(x_idx, y_idx) - last_ng_idx
    
print(ans)
