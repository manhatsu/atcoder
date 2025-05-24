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

N, K, P = map(int, input().split())

C = []
A = []
for i in range(N):
    l = list(map(int, input().split()))
    C.append(l[0])
    A.append(l[1:])

dp = dict()
dp['0'*K] = 0

for i in range(N):
    new_dp = dp.copy()
    kaihatsuan = A[i]
    for k, v in dp.items():
        s = ''
        for j in range(K):
            now_param_val = int(k[j])
            new_param_val = min(P, now_param_val + int(kaihatsuan[j]))
            s += str(new_param_val)
        if s in new_dp:
            new_dp[s] = min(new_dp[s], v+C[i])
        else:
            new_dp[s] = v+C[i]

    dp = new_dp

ans = -1
if str(P)*K in dp:
    ans = dp[str(P)*K]

print(ans)


