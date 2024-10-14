# from collections import defaultdict, deque
# from itertools import combinations, permutations
# import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, M = map(int, input().split())

T = [False]*N

for i in range(M):
    a, b = input().split()
    a = int(a)-1
    if b == 'M':
        if T[a] == False:
            print('Yes')
            T[a] = True
            continue
    print('No')



