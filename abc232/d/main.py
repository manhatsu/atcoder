from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
sys.set_int_max_str_digits(10000000)
sys.setrecursionlimit(4100000)
import heapq
try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

H, W = map(int, input().split())
# A = list(map(int, input().split()))

F = []
for i in range(H):
    F.append(input())

ans = 0
seen = [[0]*W for _ in range(H)]
seen[0][0] = 1

def dfs(i, j, cnt):
    
    for di, dj in ((1, 0), (0, 1)):
        ni, nj = i + di, j + dj
        if 0 <= ni < H and 0 <= nj < W and F[ni][nj] == '.':
            if seen[ni][nj] >= cnt+1:
                continue
            seen[ni][nj] = cnt + 1
            dfs(ni, nj, cnt + 1)

dfs(0, 0, 1)
for i in range(H):
    for j in range(W):
        if seen[i][j] > ans:
            ans = seen[i][j]
print(ans)
