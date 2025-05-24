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

# N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

S = input()
T = S[::-1] + '_' + S
N = len(S)*2+1

dp = [0]*N
j = 0

for i in range(1, N):
    j = dp[i-1]
    while j > 0 and T[i] != T[j]:
        j = dp[j-1]
    if T[i] == T[j]:
        j += 1
    dp[i] = j

L = dp[N-1]
ans = S[:len(S)-L] + S[::-1]
ans = ans[::-1]

print(ans)