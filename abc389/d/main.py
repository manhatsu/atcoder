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

R = int(input())
# N, K = map(int, input().split())


def isOK(a, b):
    c = b - 0.5
    return a**2 + c**2 <= R**2

def bs(ok, ng, a):
    if abs(ok - ng) <= 1:
        return ok
    mid = (ok + ng) // 2
    if isOK(a, mid):
        return bs(mid, ng, a)
    else:
        return bs(ok, mid, a)

temp = 0
for i in range(R):
    # print('i', i)
    a = i + 0.5
    b = bs(0, R+1, a)
    # print('b', b)
    temp += b

ans = (temp-R)*4+1
print(ans)

    

