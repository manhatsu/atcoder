# from collections import defaultdict, deque
# from itertools import combinations, permutations
# import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))
S = input()
dic = {'R':0, 'P':1, 'S':2}

# 0: rock, 1: paper, 2: scissors

points = [[0, 1, -INF], [-INF, 0, 1], [1, -INF, 0]] # [青木の手][高橋の手]

dp = [[0]*3 for i in range(N+1)]

for i in range(3):
    dp[0][i] = 0

for j in range(1, N+1):
    dp[j][0] = max(dp[j-1][1], dp[j-1][2]) + points[dic[S[j-1]]][0]
    dp[j][1] = max(dp[j-1][2], dp[j-1][0]) + points[dic[S[j-1]]][1]
    dp[j][2] = max(dp[j-1][0], dp[j-1][1]) + points[dic[S[j-1]]][2]

print(max(dp[N]))

