from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
# from icecream import # ic
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

S = input()
Q = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

D = {'A': 0, 'B': 1, 'C': 2}
invD = {0: 'A', 1: 'B', 2: 'C'}

T = []
for s in S:
    T.append(D[s])

def f(t, k):
    temp1 = T[k >> t]
    count = 0
    for i in range(min(t, k.bit_length())):
        if k & (1 << i):
            count += 1
    temp2 = count % 3
    temp3 = t % 3
    # ic(temp1, temp2, temp3)
    temp = (temp1+temp2+temp3) % 3
    # ic(temp) 
    return invD[temp]

for _ in range(Q):
    t, k = map(int, input().split())
    k -= 1
    ans = f(t, k)
    print(ans)