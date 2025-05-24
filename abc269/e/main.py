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

N = int(input())
# N, K = map(int, input().split())

def bs1(l, r):
    if r-l < 2:
        return r
    m = (l+r) // 2
    print('?', 1, m+1, 1, N, flush=True)
    T = int(input())
    if T == m+1:
        l = m
    else:
        r = m
    return bs1(l, r)

def bs2(l, r):
    if r-l < 2:
        return r
    m = (l+r) // 2
    print('?', 1, N, 1, m+1, flush=True)
    T = int(input())
    if T == m+1:
        l = m
    else:
        r = m
    return bs2(l, r)

r = bs1(-1, N)
d = bs2(-1, N)

print('!', r+1, d+1)
    
