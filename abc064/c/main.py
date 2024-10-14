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
A = list(map(int, input().split()))

c_list = [0]*9
for a in A:
    c = a // 400
    if c >= 8:
        c_list[8] += 1
    else:
        c_list[c] += 1

ans = 0
for c in c_list[:-1]:
    if c > 0:
        ans += 1


max_ans = ans + c_list[-1]

if ans == 0 and c_list[-1] != 0:
    ans = 1

print(ans, max_ans)
