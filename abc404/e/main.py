from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from operator import ge
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
sys.setrecursionlimit(4100000)
import heapq
from atcoder.segtree import SegTree
try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N = int(input())
# N, K = map(int, input().split())
C = list(map(int, input().split()))
C = [0] + C
A = list(map(int, input().split()))
A = [0] + A
B = [0]
for i, a in enumerate(A):
    if a > 0:
        B.append(i)

def get_min_step(L, R):
    step = 0
    l = R
    newl = l
    flag = False
    while True:
        step += 1
        for i in range(l, R+1):
            newl = min(newl, i - C[i])
            if newl <= L:
                flag = True
                break
        if flag:
            break
        l = newl
    return step

ans = 0
for i in range(len(B)-1):
    ans += get_min_step(B[i], B[i+1])

print(ans)