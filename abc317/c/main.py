N, M = map(int, input().split())

G = [[0]*N for _ in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    G[a-1][b-1] = c
    G[b-1][a-1] = c

ans = 0
seen = [0]*N
def dfs(idx, s):
    # print('dfs({}, {})'.format(idx, s))
    global ans
    ans = max(s, ans)
    # print('ans', ans)
    seen[idx] = 1
    # print(seen)
    for nidx in range(N):
        if (seen[nidx] == 0) and (G[idx][nidx]):
            dfs(nidx, s+G[idx][nidx])
    seen[idx] = 0
    # print(seen)

for i in range(N):
    dfs(i, 0)
    # print(seen)

print(ans)





