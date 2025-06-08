from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
try:
    from icecream import ic
except ImportError:
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

T = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

def solve(N, S):
    mid = N//2 if N % 2 == 0 else N//2 + 1
    ans = 0
    for i, s in enumerate(S[:mid]):
        ans += ((ord(s) - ord('A')) * pow(26, mid - i - 1, MOD)) % MOD
    ans %= MOD

    U = S[:mid] + S[:mid][::-1] if N % 2 == 0 else S[:mid] + S[:mid-1][::-1]
    if U <= S:
        ans += 1
    return ans % MOD

for _ in range(T):
    N = int(input())
    S = input()
    print(solve(N, S))