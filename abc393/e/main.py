from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from mimetypes import init
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, K = map(int, input().split())
A = list(map(int, input().split()))

MAX_A = max(A)

init_count = [0] * (MAX_A + 1)
div_count = [0] * (MAX_A + 1)

for a in A:
    init_count[a] += 1

for d in range(1, MAX_A+1):
    for multiple in range(d, MAX_A + 1, d):
        div_count[d] += init_count[multiple]

max_gcd_for_x = [1] * (MAX_A + 1)

for g in range(MAX_A, 0, -1):
    if div_count[g] >= K:
        for multiple in range(g, MAX_A + 1, g):
            max_gcd_for_x[multiple] = max(max_gcd_for_x[multiple], g)

for a in A:
    print(max_gcd_for_x[a])
