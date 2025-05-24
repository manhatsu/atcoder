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
# from icecream import # ic

N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

def is_ok(A, b):
    return A * pow(2*b+1, 2) <= N


def bs(ok, ng, a):
    A = pow(2, a)
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(A, mid):
            ok = mid
        else:
            ng = mid
    return ok


ans = 0
if N == 1:
    print(0)
    exit()
    
for a in range(1, int(math.log2(N))+1):
    # ic(a)
    temp = bs(-1, 10**9+1, a)
    # ic(temp)
    if temp == -1:
        continue
    ans += temp+1

print(ans)
