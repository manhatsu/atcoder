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

N, M = map(int, input().split())
# A = list(map(int, input().split()))

dhdw_list = []
for dh in range(0, int(M**0.5)+1):
    dw2 = M - dh**2
    tdw = int(dw2**0.5)
    if tdw**2 == dw2:
        dhdw_list.append((dh, tdw))

seen = [[-1]*N for i in range(N)]
seen[0][0] = 0
if len(dhdw_list) > 0:

    Q = deque([(0, 0)])

    ph = [1, -1, 1, -1]
    pw = [1, 1, -1, -1]

    while Q:
        nowh, noww = Q.popleft()
        for dh, dw in dhdw_list:
            for i in range(4):
                nexh = nowh+dh*ph[i]
                nexw = noww+dw*pw[i]
                if nexh < 0 or nexh >= N or nexw < 0 or nexw >= N:
                    continue
                if seen[nexh][nexw] != -1:
                    continue
                seen[nexh][nexw] = seen[nowh][noww] + 1
                Q.append((nexh, nexw))

for i in range(N):
    print(*seen[i])   