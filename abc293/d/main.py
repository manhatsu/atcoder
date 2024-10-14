import sys
sys.setrecursionlimit(10**8)

N, M = map(int, input().split())
# A_list = list(map(int, input().split()))

G = [[[] for i in range(2)] for j in range(N)]
for i in range(N):
    G[i][0].append((i, 1))
    G[i][1].append((i, 0))

color = {'R':0, 'B':1}

for i in range(M):
    a, b, c, d = input().split()
    a = int(a)-1
    c = int(c)-1
    G[a][color[b]].append((c, color[d]))
    G[c][color[d]].append((a, color[b]))

# print(G)

def dfs(v, w, pv, pw):
    if seen[v][w]:
        return True
    seen[v][w] = True
    for (lv, lw) in G[v][w]:
        if (lv, lw) == (pv, pw):
            continue
        if dfs(lv, lw, v, w):
            return True
    return False

cycle = 0
bar = 0
seen = [[False]*2 for i in range(N)]
for i in range(N):
    for j in range(2):
        if seen[i][j]:
            continue
        ret = dfs(i, j, -1, -1)
        if ret:
            cycle += 1
        else:
            bar += 1

print(cycle, bar)
