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

S = []
s = 0
for a in A:
    s += a
    S.append(s)

D = defaultdict(int)

for s in S:
    D[s] += 1

ans = 0
for k, v in D.items():
    ans += v*(v-1)//2
    if k == 0:
        ans += v

print(ans)