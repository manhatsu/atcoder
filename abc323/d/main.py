# from collections import defaultdict, deque
# from itertools import combinations, permutations
# import math
from email.policy import default
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N = int(input())

def getOrig(s, c):
    while s % 2 == 0:
        s //= 2
        c *= 2
    return s, c

D = defaultdict(int)

for i in range(N):
    s, c = map(int, input().split())
    s, c = getOrig(s, c)
    D[s] += c

ans = 0

for v in D.values():
    ans += v.bit_count()

print(ans)

    
