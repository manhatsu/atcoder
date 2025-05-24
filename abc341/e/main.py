# from collections import defaultdict, deque
# from itertools import combinations, permutations
# import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
from sortedcontainers import SortedList
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, Q = map(int, input().split())
S = input()
# A = list(map(int, input().split()))

B = SortedList([])
if N > 1:
    for i in range(1, N):
        if S[i] == S[i-1]:
            B.add(i-1)

def invert(l, r):
    if l > 0:
        if (l-1) in B:
            B.discard(l-1)
        else:
            B.add(l-1)
    if r < N-1:
        if r in B:
            B.discard(r)
        else:
            B.add(r)

def judge(l, r):
    # if l == r:
        # print('Yes')
        # return
    # if (l in B) or (r-1 in B): # TLEする
        # print('No')
        # return
    
    right = bisect_right(B, l-1)
    if right == len(B) or B[right] > r-1:
        print('Yes')
    else:
        print('No')
    return

for _ in range(Q):
    q, l, r = map(int, input().split())
    l, r = l-1, r-1

    if q == 1:
        invert(l, r)
    else:
        judge(l, r)
