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

N, K = map(int, input().split())
A = list(map(int, input().split()))

idx_of_1 = -1
for i, a in enumerate(A):
    if a == 1:
        idx_of_1 = i
        break

ans = 0
ans += i // (K-1)
rem = 0
if i % (K-1) != 0:
    ans += 1
    rem = K-1 - i % (K-1)
if N-i-1-rem > 0:
    ans += (N-i-1-rem) // (K-1)
    if (N-i-1-rem) % (K-1) != 0:
        ans += 1

print(ans)