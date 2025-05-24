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
# A = list(map(int, input().split()))

def F(N):
    for i in range(2, int(N**(1/3))+1):
        if N%i == 0:
            if N%(i*i) == 0:
                p = i
                q = N // (i*i)
                return p, q
            else:
                q = i
                p = int(math.sqrt(N//i))
                return p, q
            
    return None, None
            
for _ in range(T):
    t = int(input())
    p, q = F(t)
    print(p, q)