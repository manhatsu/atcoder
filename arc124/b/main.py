from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from operator import xor
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N = int(input())
# N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

################################
# a^b = x <=> a^x = b <=> b^x = a
# a^a = 0で、xorの計算に影響しないから
################################

xor_list = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        xor_list[i][j] = A[i]^B[j]

ans = set()

D = defaultdict(list)
for i in range(N):
    for j in range(N):
        D[xor_list[i][j]].append((i, j))

def dfs(i, k, used_j_index):
    if i == N:
        ans.add(k)
        return
    if i == 0:
        for j in range(N):
            used_j_index.add(j)
            dfs(i+1, xor_list[i][j], used_j_index)
            used_j_index.remove(j)
        return
    else:
        for j in range(N):
            if j in used_j_index:
                continue
            if xor_list[i][j] != k:
                continue
            used_j_index.add(j)
            dfs(i+1, k, used_j_index)
            used_j_index.remove(j)
        return

dfs(0, 0, set())
print(len(ans))
ans = sorted(list(ans))

for a in ans:
    print(a)
    

for k, v in D.items():
    if len(v) < N:
        continue

    def dfs(i, j, selected_num):
        if selected_num == N:
            ans.add(k)
            return

        for ni, nj in D[k]:
            if ni == i or nj == j:
                continue
            dfs(ni, nj, selected_num+1)
        