from collections import defaultdict, deque
from hmac import new
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

N = int(input())
# N, K = map(int, input().split())
A = input()

dp0 = deque()
dp1 = deque()

for a in A:
    if a == '0':
        dp0.append(0)
        dp1.append(1)
    else:
        dp0.append(1)
        dp1.append(0)

while len(dp0) > 1:
    new_dp0 = deque()
    new_dp1 = deque()
    while dp0:
        a = dp0.popleft()
        b = dp0.popleft()
        c = dp0.popleft()
        new_dp0.append(sum([a, b, c]) - max(a, b, c))
    while dp1:
        a = dp1.popleft()
        b = dp1.popleft()
        c = dp1.popleft()
        new_dp1.append(sum([a, b, c]) - max(a, b, c))
    dp0 = new_dp0
    dp1 = new_dp1

print(dp0[0] + dp1[0])


