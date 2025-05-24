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
ans = 0

for i, s in enumerate(S):
    if i == 0 or i == len(S)-1:
        continue
    if s == 'B':
        sub0 = S[:i][::-1]
        sub1 = S[i+1:]
        for j in range(min(len(sub0), len(sub1))):
            if sub0[j] == 'A' and sub1[j] == 'C':
                ans += 1
        
print(ans)