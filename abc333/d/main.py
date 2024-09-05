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

G = [[] for _ in range(N)]
for i in range(N-1):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    G[u].append(v)
    G[v].append(u)

count_list = []
seen = [0]*N
seen[0] = 1
if len(G[0]) == 1:
    ans = 1
else:
    for lv in G[0]:
        seen[lv] = 1
        count = 1
        Q = deque()
        Q.append(lv)
        while Q:
            v = Q.popleft()
            for lv in G[v]:
                if seen[lv] != 0:
                    continue
                seen[lv] = 1
                count += 1
                Q.append(lv)

        count_list.append(count)
    ans = sum(count_list)-max(count_list)+1

print(ans)

