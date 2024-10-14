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

T = int(input())
# N, K = map(int, input().split())

# 最大公約数
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
# 最小公倍数
def lcm(a, b):
    d = gcd(a, b)
    return int(a/d*b)

for i in range(T):
    N, D, K = map(int, input().split())
    if K == 1:
        ans = 0
    else:
        ans = (K-1)*D%N+(K-1)//(lcm(N, D)//D)
    print(ans)