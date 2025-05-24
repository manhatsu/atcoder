from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
from functools import lru_cache
# from icecream import # ic
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, M = map(int, input().split())
# A = list(map(int, input().split()))
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

# ic(A)
if N == 1:
    print(A[0][0] % M)
    exit()

@lru_cache(None)
def dfs(h, w, mod_val):
    if h == N-1 and w == N-1:
        new_val = (mod_val * 10 + A[h][w]) % M
        return new_val

    max_val = 0
    for dh, dw in [(1, 0), (0, 1)]:
        nh, nw = h + dh, w + dw
        if nh < N and nw < N:
            new_mod = (mod_val * 10 + A[h][w]) % M
            max_val = max(max_val, dfs(nh, nw, new_mod))
    return max_val

print(dfs(0, 0, 0))

# L = list(combinations(range(2*(N-1)), N-1))

# ans = 0
# for l in L:
#     nh = 0
#     nw = 0
#     S = ''
#     S += str(A[0][0])
#     q = deque(l)
#     for i in range(2*(N-1)):
#         # ic(i)
#         if not q:
#             nh += 1
#         elif q[0] != i:
#             nh += 1
#         else:
#             q.popleft()
#             nw += 1
#         # ic(nh, nw)
#         S += str(A[nh][nw])
#     ans = max(ans, int(S)%M)

# print(ans)





