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

H, W, D = map(int, input().split())
# A = list(map(int, input().split()))

F = []
for i in range(H):
    F.append(input())

dh = [0, 1, 0, -1]
dw = [1, 0, -1, 0]

seen = [[-1] * W for i in range(H)]

Q = deque()

for i in range(H):
    for j in range(W):
        if F[i][j] == 'H':
            seen[i][j] = 0
            Q.append((i, j))
            

while Q:
    nowh, noww = Q.popleft()
    if seen[nowh][noww] == D:
        continue
    for i in range(4):
        nexh = nowh + dh[i]
        nexw = noww + dw[i]
        if nexh < 0 or nexh >= H or nexw < 0 or nexw >= W:
            continue
        if F[nexh][nexw] == '#':
            continue
        if seen[nexh][nexw] >= 0:
            continue
        seen[nexh][nexw] = seen[nowh][noww] + 1
        Q.append((nexh, nexw))

ans = 0
for i in range(H):
    ans += sum([seen[i][j] >= 0 for j in range(W)])

print(ans)
