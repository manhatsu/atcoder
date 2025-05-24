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

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

G = [set() for _ in range(N)]
for i in range(M):
    a, b = A[i], B[i]
    a -= 1
    b -= 1
    G[a].add(b)
    G[b].add(a)

seen = [-1]*N

for i in range(N):
    if seen[i] != -1:
        continue
    seen[i] = 0
    Q = deque([i])
    while Q:
        q = Q.popleft()
        for lq in G[q]:
            if seen[lq] != -1:
                if seen[lq] == seen[q]:
                    print("No")
                    exit()
                continue
            seen[lq] = 1 - seen[q]
            Q.append(lq)

print("Yes")