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
from atcoder.dsu import DSU

N, M = map(int, input().split())
# A = list(map(int, input().split()))
E = []
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    if a > b:
        a, b = b, a
    E.append((a, b))

E = sorted(E)

U = DSU(N)
ans = [0]
now = 0

for i in reversed(range(N)):
    now += 1
    while E and E[-1][0] == i:
        a, b = E.pop()
        if U.same(a, b):
            continue
        U.merge(a, b)
        now -= 1
    ans.append(now)

ans = ans[::-1]
print(*ans[1:], sep="\n")
