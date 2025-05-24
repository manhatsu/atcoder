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
A = list(map(int, input().split()))

N = [0]*14

for a in A:
    N[a] += 1

N = sorted(N)[::-1]
if N[0] >= 3 and N[1] >= 2:
    ans = True
else:
    ans = False

print('Yes' if ans else 'No')