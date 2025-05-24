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

S = input()
K = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

R = []
prev = S[0]
renketsu = 1
for s in S[1:]:
    if s == prev:
        renketsu += 1
        continue
    R.append((prev, renketsu))
    prev = s
    renketsu = 1
R.append((prev, renketsu))

if len(R) == 1:
    ans = R[0][1]//2*K
    if R[0][1]%2 != 0:
        ans += K//2
else:
    ans = 0
    for p, r in R:
        ans += r // 2 * K
    if R[0][0] == R[-1][0]:
        if R[0][1] % 2 != 0 and R[-1][1] %2 != 0:
            ans += K-1

print(ans)

