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

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A)
S = []
s = 0
for a in A:
    s += a
    S.append(s)

def f(x):
    idx = bisect_left(A, x)
    ret = 0
    if idx > 0:
        ret += x*idx - S[idx-1]
    if idx < N:
        ret += S[N-1] - (S[idx-1] if idx > 0 else 0) - x*(N-idx)
    return ret

for _ in range(Q):
    x = int(input())
    print(f(x))
