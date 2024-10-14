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
N = int(input())

T = ''
for s in S:
    if s == '1':
        T += '1'
    else:
        T += '0'

T = int(T, 2)

if T > N:
    T = -1
else:
    for i, s in enumerate(S):
        if s == '?':
            if (T | 1 << (len(S)-1-i)) <= N:
                T |= 1 << (len(S)-1-i)

print(T)