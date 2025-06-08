from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys

sys.setrecursionlimit(4100000)
import heapq
try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

X = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

X = str(X)

x = int(X[0])

ans = -1
for d in range(-9, 10):
    temp = x
    S = [x]
    ret = True
    for i in range(1, len(X)):
        if temp + d < 0 or temp + d > 9:
            ret = False
            break
        temp += d
        S.append(temp)
    if not ret:
        continue
    S_int = int(''.join(map(str, S)))
    if ret and S_int >= int(X):
        ans = S_int
        break

if ans == -1:
    x = int(X[0]) + 1
    for d in range(-9, 10):
        temp = x
        S = [x]
        ret = True
        for i in range(1, len(X)):
            if temp + d < 0 or temp + d > 9:
                ret = False
                break
            temp += d
            S.append(temp)
        if not ret:
            continue
        S_int = int(''.join(map(str, S)))
        if ret and S_int >= int(X):
            ans = S_int
            break

print(ans)