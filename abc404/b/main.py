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

N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

S = []
for _ in range(N):
    S.append(input())

T = []
for _ in range(N):
    T.append(input())

def rotate_90deg(S):
    ret = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ret[j][N-1-i] = S[i][j]
    return ret

ans = INF
for i in range(4):
    temp_ans = i
    # ic(S)
    for j in range(N):
        for k in range(N):
            if S[j][k] != T[j][k]:
                temp_ans += 1
    ans = min(ans, temp_ans)
    S = rotate_90deg(S)

print(ans)

