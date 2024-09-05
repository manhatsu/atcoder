# from collections import defaultdict, deque
# from itertools import combinations, permutations
# import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, Q = map(int, input().split())
A = sorted(list(map(int, input().split())))

def is_ok(x, b, k):
    idx0 = bisect_left(A, b-x)
    idx1 = bisect_right(A, b+x)
    return idx1-idx0 < k

def bs(ok, ng, b, k): # okの初期値は-1, ngの初期値は最大idx+1
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        # print('search', mid)
        if is_ok(mid, b, k):
            ok = mid
        else:
            ng = mid
    return ok

for i in range(Q):
    b, k = map(int, input().split())
    d = bs(-1, 2*(10**8)+1, b, k) + 1
    print(d)

