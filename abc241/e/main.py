from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from numpy import add
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
sys.setrecursionlimit(4100000)
try:
    from icecream import ic
except ImportError:
    # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")


N, K = map(int, input().split())
A = list(map(int, input().split()))

seen = [-1]*N
seen[0] = 0

candies_modn = A[0] % N

loop_start_idx = -1
Q = deque()
Q.append(0)
while True:
    if seen[candies_modn] != -1:
        loop_start_idx = candies_modn
        break
    Q.append(candies_modn)
    seen[candies_modn] = len(Q) - 1
    candies_modn = (candies_modn + A[candies_modn]) % N

# ic(loop_start_idx)
# ic(Q)

added = 0
ans = 0
while True:
    idx = Q.popleft()
    if idx == loop_start_idx:
        Q.appendleft(idx)
        break
    ans += A[idx]
    added += 1
    if added == K:
        print(ans)
        exit()
# ic(added, ans)
# ic(Q)

S = []
s = 0
while Q:
    idx = Q.popleft()
    s += A[idx]
    S.append(s)

# ic(S)
rem = K - added
ans += S[-1] * ((rem-1) // len(S)) + S[(rem-1) % len(S)]
print(ans)