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

N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))


if N == 0 or N%2 == 1:
    print(0)
    exit()

ans= N//10

# 5の何乗まで含むか
temp = 5**2*2
while True:
    if N < temp:
        break
    ans += N//temp
    temp *= 5

print(ans)