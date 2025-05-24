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

head = []
tail = []
hantenFlag = False

for s in S:
    if s == 'R':
        hantenFlag = not hantenFlag
        continue
    if hantenFlag:
        head.append(s)
    else:
        tail.append(s)

if hantenFlag:
    T = tail[::-1] + head
else:
    T = head[::-1] + tail


A = []

for t in T:
    if len(A) == 0:
        A.append(t)
        continue
    if A[-1] == t:
        A.pop()
    else:
        A.append(t)

print(''.join(A))

