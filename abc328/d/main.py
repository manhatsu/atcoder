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

S = input()

Q = ''
for s in S:
    Q += s
    if len(Q) >= 3 and Q[-3:] == 'ABC':
        Q = Q[:-3]
    
print(Q)