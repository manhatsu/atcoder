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

S = input()
# N, K = map(int, input().split())
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ans = 0
for l in alphabet:
    temp = 0
    toadd = 0
    for s in S:
        if s == l:
            ans += temp
            temp += toadd
            toadd += 1
        else:
            temp += toadd
    # print(ans)

print(ans)
            

