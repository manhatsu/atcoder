N = int(input())

E = [[0]*N for i in range(N)]

for i in range(N-1):
    D = list(map(int, input().split()))
    # for j, d in enumerate(D):
        # E[i][i+j+1] = d
        # E[i+j+1][i] = d
    for j in range(i + 1, N):
        E[i][j] = E[j][i] = D[j - i - 1]

# print(E)

def dfs(used):
    # print('called dfs(used)')
    # print('used list:', used)
    if all(used):
        return 0
    v = used.index(False)
    # print('used v:', v, 'turned into True')
    ret = 0
    used[v] = True
    for w in range(v+1, len(used)):
        # print('used w:', w, 'turned into True')
        if not used[w]:
            used[w] = True
            temp = E[v][w] + dfs(used)
            if ret < temp:
                # print('ret updated to', temp)
                ret = temp
            used[w] = False
            # print('used w:', w, 'turned into False')
    used[v] = False
    # print('used v:', v, 'turned into False')
    return ret

ans = 0
used = [False]*N
if N%2 == 0:
    ans = dfs(used)
else:
    for v in range(N):
        used[v] = True
        ans = max(ans, dfs(used))
        used[v] = False

print(ans)