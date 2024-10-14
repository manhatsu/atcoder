from collections import defaultdict, deque
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

W,H = map(int, input().split())
N = int(input())
S = []
for i in range(N):
    p, q = map(int, input().split())
    S.append((p, q))

a = int(input())
A = list(map(int, input().split()))
b = int(input())
B = list(map(int, input().split()))

G = defaultdict(int)

for p, q in S:
    x = bisect_left(A, p)
    y = bisect_right(B, q)
    G[(x, y)] += 1

# print(G)

ans_max = 0
ans_min = 10**6
for key, val in G.items():
    ans_max = max(ans_max, val)
    ans_min = min(ans_min, val)

if len(G) < (a+1)*(b+1):
    ans_min = 0

print(ans_min, ans_max)