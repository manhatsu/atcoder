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
M = int(input())
B = set(list(map(int, input().split())))
X = int(input())

dp = [0]*(X+1)
dp[0] = 1

for i in range(X):
    if dp[i] == 0:
        continue
    for a in A:
        if i+a <= X and i+a not in B:
            dp[i+a] = 1

print('Yes' if dp[X] == 1 else 'No')