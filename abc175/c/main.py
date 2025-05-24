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

X, K, D = map(int, input().split())
if abs(X) > K*D:
    if X >= 0:
        ans = X - K*D
    else:
        ans = X + K*D
else:
    J = abs(X)//D
    
    if K % 2 == J % 2:
        Z = J*D
        if X >= 0:
            ans = X-Z
        else:
            ans = X+Z
    else:
        if X >= 0:
            ans0 = X-(J-1)*D
            ans1 = X-(J+1)*D
            if abs(ans0) >= abs(ans1):
                ans = ans1
            else:
                ans = ans0
        else:
            ans0 = X-(J-1)*D
            ans1 = X+(J+1)*D
            if abs(ans0) >= abs(ans1):
                ans = ans1
            else:
                ans = ans0

print(abs(ans))