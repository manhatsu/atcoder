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

N = int(input())
# N, K = map(int, input().split())
A = list(map(int, input().split()))

sum = 0
last_seen = {}
temp = 0
for i, a in enumerate(A):
    toadd = 0
    if a not in last_seen:
        toadd = i+1
        temp += toadd
        sum += temp
        last_seen[a] = i
    else:
        toadd = i+1-(last_seen[a]+1)
        last_seen[a] = i
        temp += toadd
        sum += temp
    # print(sum)

print(sum)

