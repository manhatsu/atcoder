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

S = input()
# N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

stack = []
box = set()
ret = True
for s in S:
    if s == '(':
        stack.append(s)
    elif s == ')':
        while stack[-1] != '(':
            l = stack.pop()
            box.discard(l)
        stack.pop()
    else:
        if s in box:
            ret = False
            break
        box.add(s)
        stack.append(s)

print('Yes' if ret else 'No')
