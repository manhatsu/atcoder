from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from platform import mac_ver
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

T = int(input())

for _ in range(T):
    N = int(input())
    S = []
    for z in range(3):
        temp = input()
        S.append(temp+temp)

    ans = '0'*N + '1'*N + '0'
    print(ans)
