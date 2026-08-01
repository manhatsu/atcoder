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

T = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

def solve(N, A):
    ans = 0
    S = set()
    P = [[] for _ in range(N+1)]
    for i in range(2*N):
        P[A[i]].append(i)
    for i in range(2*N-3):
        if A[i] == A[i+1]:
            continue
        if A[i+1] == A[i+2]:
            continue
        if (A[i], A[i+1]) in S or (A[i+1], A[i]) in S:
            continue
        V = sorted(P[A[i]] + P[A[i+1]])
        if V[0] < i:
            continue
        if V[0] + 1 == V[1] and V[2] + 1 == V[3]:
            ans += 1
            S.add((A[i], A[i+1]))
    return ans
    
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    result = solve(N, A)
    print(result)