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

G = [set() for i in range(N)]
for i in range(M):
    a = A[i]-1
    b = B[i]-1
    G[a].add(b)
    G[b].add(a)

# print(G)

seen = [-1]*N
Q = deque()
ans = True
for i in range(N):
    if seen[i] == -1:
        seen[i] = 0
        Q.append(i)
        while Q:
            v = Q.popleft()
            next_bit = 1 - seen[v]
            for lv in G[v]:
                if seen[lv] == -1:
                    seen[lv] = next_bit
                    Q.append(lv)
                    continue
                if seen[lv] != next_bit:
                    ans = False
                    break
            if not ans:
                break
    if not ans:
        break

print('Yes' if ans else 'No')

