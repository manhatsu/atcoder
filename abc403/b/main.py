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

T = input()
U = input()


for i in range(len(T)):
    ret = True
    for j in range(len(U)):
        if i+j >= len(T):
            ret = False
            break
        if T[i+j] != '?' and T[i+j] != U[j]:
            ret = False
            break
    if ret:
        print("Yes")
        exit()
print("No")