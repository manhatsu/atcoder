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

N, K = map(int, input().split())
A = list(map(int, input().split()))

S = []
SD = defaultdict(int)
temp = 0
for a in A:
    temp += a
    S.append(temp)
    SD[temp] += 1

ans = 0
offset = 0
for i in range(N):
    if K+offset in SD:
        ans += SD[K+offset]
    offset += A[i]
    SD[S[i]] -= 1
print(ans)