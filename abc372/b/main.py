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

M = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

temp = 1
threes = [1]
for i in range(10):
    temp *= 3
    threes.append(temp)

threes = threes[::-1]
# print(threes)

ans = []
for i, t in enumerate(threes):
    if M // t > 0:
        q = M // t
        M = M - q*t
        for j in range(q):
            ans.append(10-i)

print(len(ans))
print(*ans[::-1])
    



