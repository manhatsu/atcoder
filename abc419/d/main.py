from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
sys.set_int_max_str_digits(10000000)
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

N, M = map(int, input().split())
S = input()
T = input()

I = [0]*N
for i in range(M):
    l, r = map(int, input().split())
    I[l-1] += 1
    if r < N:
        I[r] -= 1

# for j in range(N):
#     if I[j] > 0 and I[j] % 2 != 0:
#         I[j] = 1
#     elif I[j] < 0 and I[j] % 2 != 0:
#         I[j] = -1
#     else:
#         I[j] = 0
    
J = [I[0]]
for i in range(1, N):
    J.append(J[i-1] + I[i])

ans = []
for i in range(N):
    if J[i] % 2 == 0:
        ans.append(S[i])
    else:
        ans.append(T[i])

print("".join(ans))
