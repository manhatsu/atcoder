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

h1, h2, h3, w1, w2, w3 = map(int, input().split())

ans = 0
for h11 in range(1, h1+1):
    for h12 in range(1, h1+1-h11):
        h13 = h1 - h11 - h12
        if h13 < 1:
            continue
        for h21 in range(1, h2+1):
            for h22 in range(1, h2+1-h21):
                h23 = h2 - h21 - h22
                if h23 < 1:
                    continue
                h31 = w1-h11-h21
                h32 = w2-h12-h22
                h33 = w3-h13-h23
                if h31 >= 1 and h32 >= 1 and h33 >= 1 and h31+h32+h33 == h3:
                    ans += 1

print(ans)