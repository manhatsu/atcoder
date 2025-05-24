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

N, D = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A)

if N == 1:
    print(0)
    exit()

if D == 0:
    ans = 0
    for i in range(1, N):
        if A[i] == A[i-1]:
            ans += 1
    print(ans)
    exit()

B = [[] for _ in range(D)]

for a in A:
    j = a % D
    if len(B[j]) == 0 or B[j][-1][0] != a:
        B[j].append((a, 1))
    else:
        _, c = B[j].pop()
        B[j].append((a, c+1))

ans = 0
for j in range(D):
    if len(B[j]) == 0:
        continue
    dp = [[0]*2 for _ in range(len(B[j]))]
    dp[0][0] = B[j][0][1]
    dp[0][1] = 0
    for i in range(1, len(B[j])):
        if B[j][i][0] == B[j][i-1][0] + D:
            dp[i][0] = min(dp[i-1][0] + B[j][i][1], dp[i-1][1] + B[j][i][1])
            dp[i][1] = dp[i-1][0]
        else:
            dp[i][0] = min(dp[i-1][0] + B[j][i][1], dp[i-1][1] + B[j][i][1])
            dp[i][1] = min(dp[i-1][0], dp[i-1][1])
    
    ans += min(dp[-1][0], dp[-1][1])

print(ans)

# ans = 0
# for i, a in enumerate(A):
#     j = a % D
#     # ic(j)
#     # ic(B[j])
#     if len(B[j]) == 0:
#         B[j].append((a, 1))
#         continue
#     if B[j][-1][0] == a:
#         _, c = B[j].pop()
#         B[j].append((a, c+1))
#     elif B[j][-1][0] == a-D:
#         B[j].append((a, 1))
#     else:
#         if len(B[j]) >= 2:
#             ans += min(sum(b[1] for b in B[j][0::2]), sum(b[1] for b in B[j][1::2]))
#         B[j] = [(a, 1)]
#     # ic(B[j])

# for i in range(D):
#     if len(B[i]) >= 2:
#         ans += min(sum(b[1] for b in B[i][0::2]), sum(b[1] for b in B[i][1::2]))

# print(ans)
    


