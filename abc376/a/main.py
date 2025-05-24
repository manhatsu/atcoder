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

N, C = map(int, input().split())
T = list(map(int, input().split()))

ans = 0
prev_t = 0
for i in range(N):
    if i == 0:
        ans += 1 
        prev_t = T[i] 
    elif T[i]-prev_t >= C:
        ans += 1
        prev_t = T[i]

print(ans)
    
            
