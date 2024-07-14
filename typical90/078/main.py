N, M = map(int, input().split())
# A_list = list(map(int, input().split()))

G = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

G = [sorted(g) for g in G]

ans = 0
for i, g in enumerate(G):
    if i == 0:
        continue
    count = 0
    for l in g:
        if l >= i:
            break
        count += 1
        if count > 1:
            break
    if count == 1:
        ans += 1

print(ans)






