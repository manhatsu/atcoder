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

N = int(input())
X = list(map(int, input().split()))
P = list(map(int, input().split()))

zzip = zip(X, P)
szzip  =sorted(zzip)
X, P = zip(*szzip)
# print(X, P)

S = []
temp = 0
for p in P:
    temp += p
    S.append(temp)

Q = int(input())

def getS(l, r):
    left = bisect_left(X, l)
    right = bisect_right(X, r)
    if left >= N or right == 0:
        return 0
    if right - 1 < 0:
        return 0
    elif left == 0:
        return S[right-1]
    else:
        return S[right-1] - S[left-1]

for q in range(Q):
    l, r = map(int, input().split())
    ans = getS(l, r)
    print(ans)


