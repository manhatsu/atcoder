from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
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
for _ in range(H):
    F.append(list(map(int, input().split())))

seen = [[0]*W for _ in range(H)]
d = [(0, 1), (1, 0)]

def calc_xor(seen):
    ret = 0
    for h in range(H):
        for w in range(W):
            if seen[h][w] < 2:
                ret ^= F[h][w]
    return ret

ans = calc_xor(seen)

def dfs(seen):
    global ans
    ans = max(ans, calc_xor(seen))
    for h in range(H):
        for w in range(W):
            if seen[h][w] > 0:
                continue
            seen[h][w] = 1
            for k in range(2):
                nh = h + d[k][0]
                nw = w + d[k][1]
                if 0 <= nh < H and 0 <= nw < W and seen[nh][nw] == 0:
                    seen[nh][nw] = seen[h][w] = 2
                    dfs(seen)
                    seen[nh][nw] = 0
                    seen[h][w] = 1
            dfs(seen)
            seen[h][w] = 0
            return
    
dfs(seen)
print(ans)
