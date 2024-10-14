# from collections import defaultdict, deque
from itertools import combinations, permutations
# import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

S, T, U = input().split()

brothers = [0, 1, 2]

orders = list(permutations(brothers))

for order in orders:
    if S == '<':
        if order[0] > order[1]:
            continue
    elif S == '>':
        if order[1] > order[0]:
            continue
    if T == '<':
        if order[0] > order[2]:
            continue
    elif T == '>':
        if order[2] > order[0]:
            continue
    if U == '<':
        if order[1] > order[2]:
            continue
    elif U == '>':
        if order[2] > order[1]:
            continue
    ans = order
    break

ret = ['A', 'B', 'C']
print(ret[ans.index(1)])



