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
P = list(map(int, input().split()))

sousa = 0
S = []

for i in range(1, N):
    if P[i-1] > P[i]:
        sousa += 1
        S.append(i+1, i-1)
        temp = P[i-1]
        P[i-1] = P[i]
        P[i] = P[i+1]
        P[i+1] = temp
    
