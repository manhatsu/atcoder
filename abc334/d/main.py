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

N ,Q = map(int, input().split())
R = sorted(list(map(int, input().split())))

S = []
temp = 0
for r in R:
    temp += r
    S.append(temp)

for _ in range(Q):
    q = int(input())
    print(bisect_right(S, q))