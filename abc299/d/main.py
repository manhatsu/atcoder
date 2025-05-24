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

def bs(l, r):
    if abs(r-l) <= 1:
        return l
    m = (l+r)//2
    print(f"? {m}", flush=True)

    s = int(input())
    if s == 0:
        l = m
    else:
        r = m
    return bs(l, r)

N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

ret = bs(0, N)
print(f"! {ret}")
