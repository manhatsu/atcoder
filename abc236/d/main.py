from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
try:
    from icecream import ic
except ImportError:
    # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))
A = [[-1]*(2*N) for _ in range(2*N)]
for i in range(2*N-1):
    B = list(map(int, input().split()))
    for j in range(i+1, 2*N):
        A[i][j] = B[j-i-1]
        A[j][i] = B[j-i-1]

ans = 0

def dfs(state, val):
    if state == (1 << (2*N)) - 1:
        global ans
        ans = max(ans, val)
        return
    
    for i in range(2*N):
        if state & (1 << i):
            continue
        for j in range(i+1, 2*N):
            if state & (1 << j):
                continue
            new_state = state | (1 << i) | (1 << j)
            dfs(new_state, val ^ A[i][j])
        break # 選ぶ順序で答えが変わらないので、常に1つ目の人iを選ぶ

dfs(0, 0)
print(ans)