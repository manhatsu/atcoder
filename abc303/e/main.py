from collections import deque
from re import S
N = int(input())
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))

G = [[] for i in range(N)]
for i in range(N-1):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    G[u].append(v)
    G[v].append(u)

for i in range(N):
    if len(G[i]) == 1:
        start = i
        break


ans = []
Q = deque()
ini_c = G[start][0]
ans.append(len(G[ini_c]))

for lv in G[ini_c]:
    if len(G[lv]) == 2:
        Q.append((lv, ini_c))

while Q:
    nv, pv = Q.popleft()
    # print('nv:', nv, 'pv:', pv)
    for lv in G[nv]:
        if lv == pv:
            continue
        for mv in G[lv]:
            if mv == nv:
                continue
            ans.append(len(G[mv]))
            for ov in G[mv]:
                if ov == lv:
                    continue
                if len(G[ov]) == 2:
                    Q.append((ov, mv))

ans = sorted(ans)

print(*ans)
    





