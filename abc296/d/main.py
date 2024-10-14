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

N, M = map(int, input().split())

min_diff = INF
ans = -1
maxa = min(N, int(M**0.5)+1)
# print(maxa)
for a in range(1, maxa+1):
    if M % a == 0:
        b = M // a
    else:
        b = M // a + 1
    if b > N:
        continue
    if a*b - M < min_diff:
        # print(a, b)
        min_diff = a*b-M
        ans = a*b

print(ans)

