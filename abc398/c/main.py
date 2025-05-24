from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from re import S
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

D = defaultdict(int)
who_has = defaultdict(list)

for i, a in enumerate(A):
    D[a] += 1
    who_has[a].append(i+1)

ans = -1
for key, val in D.items():
    if val == 1:
        ans = max(ans, key)

print(who_has[ans][0] if ans != -1 else -1)