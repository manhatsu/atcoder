from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
# from icecream import # ic
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

D = dict()

G = [[] for i in range(2*N)]
for _ in range(N):
    s, t = input().split()
    if s not in D:
        D[s] = len(D)
    if t not in D:
        D[t] = len(D)
    G[D[s]].append(D[t])

# ic(D)
# ic(G)

seen = [False] * len(D)
on_stack = [False] * len(D)

def dfs(v):
    seen[v] = True
    on_stack[v] = True
    
    for lv in G[v]:
        if on_stack[lv]:
            return False
        if not seen[lv] and not dfs(lv):
            return False
    
    on_stack[v] = False
    return True

ans = True

for i in range(len(D)): 
    if not seen[i]:
        if not dfs(i):
            ans = False
            break
    
print('Yes' if ans else 'No')