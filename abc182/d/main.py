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

N = int(input())
# N, K = map(int, input().split())
A = list(map(int, input().split()))

if N == 1:
    ans = max(0, A[0])
    print(ans)
    exit()


S = []
s = 0
for a in A:
    s += a
    S.append(s)

max_idx = [0]*N
max_idx[0] = 0
temp_max_idx = 0
temp_max = S[0]
for i, s in enumerate(S[1:], start=1):
    if s > temp_max:
        temp_max = s
        temp_max_idx = i
    max_idx[i] = temp_max_idx

# print(max_idx)

# print(*S)

ans = 0
now = 0
for i, s in enumerate(S):
    temp = now + S[max_idx[i]]
    ans = max(ans, temp)
    now += s

print(ans)
