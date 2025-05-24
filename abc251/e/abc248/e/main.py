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

N, K = map(int, input().split())
# A = list(map(int, input().split()))

P = []
for i in range(N):
    P.append(tuple(map(int, input().split())))

if K == 1:
    print('Infinity')
    exit()

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a

D = defaultdict(set)
E = defaultdict(set) # x軸に平行なもの
F = defaultdict(set) # y軸に平行なもの

for i, p in enumerate(P):
    for j, q in enumerate(P):
        if i >= j:
            continue
        a = p[1] - q[1]
        da = p[0] - q[0]
        if a == 0: # x軸に平行
            E[p[1]].add(i)
            E[p[1]].add(j)
            continue
        if da == 0: # y軸に平行
            F[p[0]].add(i)
            F[p[0]].add(j)
            continue
        g = gcd(abs(a), abs(da))
        a //= g
        da //= g
        if da < 0:
            a = -a
            da = -da
        b = p[1]*da - p[0]*a
        D[(a, da, b)].add(i)
        D[(a, da, b)].add(j)

ans = 0
for k, v in D.items():
    if len(v) >= K:
        ans += 1
for k, v in E.items():
    if len(v) >= K:
        ans += 1
for k, v in F.items():
    if len(v) >= K:
        ans += 1

print(ans)


