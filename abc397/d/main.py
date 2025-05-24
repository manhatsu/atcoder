from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from operator import is_
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
# A = list(map(int, input().split()))

for X in range(1, 10**6+1):
    if 9*X**4 - 12*X*(X**3-N) <= 0:
        continue
    B = math.sqrt(9*X**4 - 12*X*(X**3-N))
    if B.is_integer() and B > 0:
        A = -3*X**2 + B
        if A > 0 and A % (6*X) == 0:
            y = A // (6*X)
            x = X + y
            if x > 0 and y > 0:
                print(int(x), int(y))
                exit()
    elif B.is_integer() and B < 0:
        A = -3*X**2 - B
        if A > 0 and A % (6*X) == 0:
            y = A // (6*X)
            x = X + y
            if x > 0 and y > 0:
                print(int(x), int(y))
                exit()
        
print(-1)
