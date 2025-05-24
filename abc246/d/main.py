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

if N == 0:
    print(0)
    exit()


def is_ok(alpha, beta):
    temp = alpha * (alpha ** 2 + beta ** 2)
    return temp >= 2*N

def bs(l, r, alpha):
    while abs(r - l) > 1:
        mid = (l + r) // 2
        if is_ok(alpha, mid):
            r = mid
        else:
            l = mid
    return r

# if N > 10:
    # ic.disable()

# ic(pow(N, 1/3))
# ic(pow(2*N, 1/3))


min_x = (math.ceil(pow(2*N, 1/3)))**3
# ic(min_x)
for alpha in range(math.ceil(pow(N, 1/3)), math.ceil(pow(2*N, 1/3))+1):
    beta = bs(-1, alpha, alpha)
    # ic(alpha, beta)
    # ic(alpha * (alpha ** 2 + beta ** 2) // 2, N)
    if beta == -1:
        beta = 0
    if beta % 2 != alpha % 2:
        beta += 1
    # ic(alpha, beta)
    if beta > alpha:
        continue
    min_x = min(min_x, alpha * (alpha ** 2 + beta ** 2) // 2)
    # ic(min_x)
print(min_x)
