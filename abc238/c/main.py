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

N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

ndigit = math.log10(N)
ndigit = int(ndigit+1) if ndigit == int(ndigit) else math.ceil(ndigit)

ans = 0
for i in range(ndigit-1):
    temp = 9*(10**i)%MOD
    ans += temp * (temp+1) // 2
    ans %= MOD
    # print(i, ans)

temp = N - (10**(ndigit-1)-1)
temp %= MOD
ans += temp * (temp+1) // 2
ans %= MOD

print(ans)

