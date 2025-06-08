from collections import deque
import sys
sys.setrecursionlimit(4100000)
try:
    from icecream import ic
except ImportError:
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)
N = int(input())
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(N-1):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    G[u].append(v)
    G[v].append(u)

C = list(map(int, input().split()))
tot_C = sum(C)

dist = [-1]*N
dist[0] = 0
sum_C = [0]*N

def dfs(v, pv, d):
    ret = 0
    for lv in G[v]:
        if lv == pv:
            continue
        dist[lv] = d+1
        ret += dfs(lv, v, d+1)
    sum_C[v] = ret + C[v]
    return sum_C[v]

dfs(0, -1, 0)

# ic(dist)

f0 = 0
for i in range(N):
    f0 += C[i] * dist[i]

ans = f0
Q = deque()
Q.append((0, f0))
seen = [0]*N
seen[0] = 1

while Q:
    v, f = Q.popleft()
    for lv in G[v]:
        if seen[lv]:
            continue
        seen[lv] = 1
        new_f = f + tot_C - 2*sum_C[lv]
        ans = min(ans, new_f)
        Q.append((lv, new_f))

print(ans)



