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
S = input()
# N, K = map(int, input().split())

if N < 3:
    ans = 0

else:
    ans = 0
    for i in range(1, N-1):
        if S[i] == '.':
            if S[i-1] == '#' and S[i+1] == '#':
                ans += 1

print(ans)
