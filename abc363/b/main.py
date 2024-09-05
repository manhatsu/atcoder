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

N, T, P = map(int, input().split())
L = list(map(int, input().split()))

i = 0
while True:
    count = 0
    for l in L:
        if (l+i) >= T:
            count += 1
    if count >= P:
        break
    i += 1

print(i)


