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
A = list(map(int, input().split()))
A.append(0)

stack = [(0, -1)]

ans = 0
for i in range(N+1):
    while A[i] < stack[-1][0]:
        val, idx = stack.pop()
        ans = max(ans, val*(i-stack[-1][1]-1))
    stack.append((A[i], i))
        
print(ans)




