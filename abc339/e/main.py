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

from atcoder.lazysegtree import LazySegTree

N, D = map(int, input().split())
A = list(map(int, input().split()))

def op(ele1, ele2):
    return max(ele1, ele2)


def mapping(func, ele):
    return func + ele


def composition(func_upper, func_lower):
    return func_upper + func_lower


e = -INF
id_ = 0
lst = [0]*(5*(10**5)+1)

# TODO (初期リストlst)
seg = LazySegTree(op, e, mapping, composition, id_, lst)

for a in A:
    X = seg.prod(max(1, a-D), min(len(lst), a+D+1))
    seg.set(a, max(X+1, seg.get(a)))

print(seg.prod(0, len(lst)))

