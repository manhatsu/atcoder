from collections import deque

N = int(input())

sumC = 0
G = [[] for _ in range(N)]
for i in range(N-1):
    a, b, c = map(int, input().split())
    G[a-1].append((b-1, c))
    G[b-1].append((a-1, c))
    sumC += c

dist = [-1]*N
dist[0] = 0

Q = deque()
Q.append((0, 0)) # node, distance

while Q:
    v, c = Q.popleft()
    for lv, lc in G[v]:
        if dist[lv] != -1:
            continue
        dist[lv] = c+lc
        Q.append((lv, c+lc))

e = dist.index(max(dist))

dist1 = [-1]*N
dist1[e] = 0

R = deque()
R.append((e, 0))
while R:
    v, c = R.popleft()
    for lv, lc in G[v]:
        if dist1[lv] != -1:
            continue
        dist1[lv] = c+lc
        R.append((lv, c+lc))

D = max(dist1) # diameter

print(sumC*2-D)

# ある点から始めて，全ての点を通って戻る場合，全ての経路を2回通る
# ↑から木の直径を引いた値が，全ての点を一筆書きで通るときの最短経路となる
    

