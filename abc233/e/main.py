from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
sys.set_int_max_str_digits(100000000)
sys.setrecursionlimit(4100000)
try:
    from icecream import ic
except ImportError:
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

X = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

S = []
s = 0
for x in str(X):
    s += int(x)
    S.append(s)

S = S[::-1]

kur = 0
ans = []
for i in range(len(str(X))):
    val = S[i] + kur
    q = val % 10
    ans.append(q)
    kur = val // 10

if kur > 0:
    for d in str(kur)[::-1]:
        ans.append(int(d))

ans = ans[::-1]
ans = int(''.join(map(str, ans)))
print(ans)