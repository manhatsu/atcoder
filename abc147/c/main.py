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
# from icecream import # ic

N = int(input())
# N, K = map(int, input().split())
S = []
for i in range(N):
    s = []
    a = int(input())
    for j in range(a):
        x, y = map(int, input().split())
        x -= 1
        s.append((x, y))
    S.append(s)

def isOK(i):
    for j in range(N):
        if (i >> j) & 1:
            for x, y in S[j]:
                if (i >> x) & 1 != y:
                    return False
    return True

ans = 0
for i in range(2**N):
    if isOK(i):
        ans = max(ans, i.bit_count())

print(ans)

                