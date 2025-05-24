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

A, B, C, D = map(int, input().split())
# A = list(map(int, input().split()))

MAX = A+B+C+D+1
fact = [1] * (MAX + 1)
invfact = [1] * (MAX + 1)

for i in range(1, MAX + 1):
    fact[i] = fact[i - 1] * i % MOD

invfact[MAX] = pow(fact[MAX], MOD - 2, MOD)

for i in range(MAX, 0, -1):
    invfact[i - 1] = invfact[i] * i % MOD

def nCr(n, r):
    if n == 0 and r == 0:
        return 1
    if r < 0 or r > n:
        return 0
    return fact[n] * invfact[r] % MOD * invfact[n - r] % MOD

def nCm(n, m):
    if n == 0 and m == 0:
        return 1
    return math.factorial(n) // (math.factorial(m) * math.factorial(n - m))

ans = 0
ans += nCr(A+B, A) * nCr(C+D, C) % MOD

for tC in range(1, C+1):
    temp = nCr(B-1+A+tC, B-1) * nCr(D+C-tC, D) % MOD
    ans += temp
    ans %= MOD

print(ans)