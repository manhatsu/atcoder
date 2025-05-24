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

# N = int(input())
# N, K = map(int, input().split())
S = input()
Q = int(input())
K = list(map(int, input().split()))

def getLetter(S, k): # k 1-indexed
    l = S[(k-1)%len(S)]
    block = (k-1)//(len(S))
    b = block.bit_count()
    if b % 2 != 0:
        l = l.swapcase()
    return l

for k in K:
    print(getLetter(S, k))
