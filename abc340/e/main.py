# from collections import defaultdict, deque
# from itertools import combinations, permutations
# import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
from atcoder.lazysegtree import LazySegTree
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

# N = int(input())
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def op(l, r):
    return max(l, r)

e = MINF

def mapping(lazy_upper, data_lower):
    return lazy_upper+data_lower

def composition(lazy_upper, lazy_lower):
    return lazy_upper+lazy_lower

_id = 0

T = LazySegTree(op, e, mapping, composition, _id, A)

for i in range(M):
    v = T.get(B[i])
    T.set(B[i], 0)
    C = v // N
    R = v % N
    T.apply(0, N, C)
    if R > 0:
        if B[i] < N-1:
            if R >= N-B[i]:
                T.apply(B[i]+1, N, 1)
                T.apply(0, R-N+B[i]+1, 1)
            else:
                T.apply(B[i]+1, B[i]+1+R, 1)
        else:
            T.apply(0, R, 1)

ans = []
for i in range(N):
    ans.append(T.get(i))

print(*ans)
