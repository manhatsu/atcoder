from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
# from icecream import # ic
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

A, B = map(int, input().split())

def calcNum1(n, bit):
    q = n // (2**(bit+1))
    r = n % (2**(bit+1))

    return 2**bit*q + r-2**bit+1 if r >= 2**bit else 2**bit*q

ans = ''
for bit in range(60):
    if A > 0:
        a = calcNum1(A-1, bit)
    else:
        a = 0
    b = calcNum1(B, bit)
    if (b-a) % 2 == 1:
        ans += '1'
    else:
        ans += '0'

# ic(aa)
# ic(bb)
ans = ans[::-1]
ans = int(ans, 2)
print(ans)

