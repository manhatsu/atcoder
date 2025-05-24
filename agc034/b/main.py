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
# A = list(map(int, input().split()))

s = input()
S = list(s)
# print(S)

if len(S) < 3:
    print(0)
else:
    num_A = 0
    ans = 0
    i = 0
    while i < len(S)-1:
        if S[i:i+2] == ['B', 'C']:
            ans += num_A
            i += 2
        else:
            if S[i] == 'A':
                num_A += 1
            else:
                num_A = 0
            i += 1
        # print(S)
        # print(D)

    print(ans)
        

        