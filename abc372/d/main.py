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

N = int(input())
# N, K = map(int, input().split())
H = list(map(int, input().split()))

ans = [0]*N
stack = []

if N == 1:
    ans = [0]
else:
    for i in range(N-1, -1, -1):
        ans[i] = len(stack)
        while len(stack) > 0 and H[i] >= stack[-1]:
            stack.pop()
        stack.append(H[i])
        
print(*ans)

