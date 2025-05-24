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
A = list(map(int, input().split()))

def combination(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

all = combination(N, 3)

D = defaultdict(int)
for a in A:
    D[a] += 1

for k, v in D.items():
    if v >= 3:
        all -= combination(v, 3)
    if v >= 2:
        all -= combination(v, 2) * (N - v)

print(all)