import re
from atcoder.segtree import SegTree
try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)


INF = float('inf')

W, N = map(int, input().split())
# A_list = list(map(int, input().split()))

D = []
for _ in range(N):
    l, r, v = map(int, input().split())
    D.append((l, r, v))

dp = [[-INF]*(W+1) for _ in range(N+1)]
dp[0][0] = 0
S = SegTree(max, -INF, dp[0])
for i in range(1, N+1):
    l, r, v = D[i-1]
    for j in range(W+1):
        dp[i][j] = dp[i-1][j]
        if j < l:
            continue
        prev_max = S.prod(max(0, j-r), min(j-l+1, W+1))
        if prev_max < 0:
            continue
        dp[i][j] = max(dp[i][j], v + prev_max)
    S = SegTree(max, -INF, dp[i])
    if N == 4:
        ic(dp[i][:20])
print(dp[N][W] if dp[N][W] >= 0 else -1)