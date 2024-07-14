N, X, Y = map(int, input().split())
X, Y = X-1, Y-1
# A_list = list(map(int, input().split()))

if N == 1:
    ans = [1]
else:
    G = [[] for _ in range(N)]
    for i in range(N-1):
        x, y = map(int, input().split())
        G[x-1].append(y-1)
        G[y-1].append(x-1)

    prev = [-1]*N
    prev[X] = X # 始点とわかるようになにか入れる

    from collections import deque
    Q = deque([X])
    found = False
    while Q:
        v = Q.popleft()
        for lv in G[v]:
            if prev[lv] != -1:
                continue
            prev[lv] = v
            Q.append(lv)
            if lv == Y:
                found = True
                break
        if found:
            break

    now = Y
    ans = []
    while now != X:
        ans.append(now)
        now = prev[now]
    ans.append(X)
    ans = [a+1 for a in ans]
print(*ans[::-1])


