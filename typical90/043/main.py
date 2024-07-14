H, W = map(int, input().split())
# A_list = list(map(int, input().split()))
sh, sw = map(int, input().split())
sh -= 1
sw -= 1
gh, gw = map(int, input().split())
gh -= 1
gw -= 1

INF = 1e9

F = []
for i in range(H):
    F.append(input())

# print(F[H-1][W-1])
D = [[[INF]*4 for w in range(W)] for h in range(H)]

# print(D)

dh = [1, 0, -1, 0]
dw = [0, 1, 0, -1]

from collections import deque

Q = deque()
for i in range(4):
    D[sh][sw][i] = 0
    Q.append((sh, sw, i))

while Q:
    (nowh, noww, nowa) = Q.popleft()

    # コスト0
    nexh = nowh + dh[nowa]
    nexw = noww + dw[nowa]
    if (0 <= nexh < H) and (0 <= nexw < W):
        if (F[nexh][nexw] != '#'):
            if D[nexh][nexw][nowa] > D[nowh][noww][nowa]:
                D[nexh][nexw][nowa] = D[nowh][noww][nowa]
                Q.appendleft((nexh, nexw, nowa))    

    # コスト1
    for i in range(4):
        if i == nowa:
            continue
        if D[nowh][noww][i] > D[nowh][noww][nowa] + 1:
            D[nowh][noww][i] = D[nowh][noww][nowa] + 1
            Q.append((nowh, noww, i))

ans = min([D[gh][gw][i] for i in range(4)])

print(ans)

# 01BFS
# 今までよりも小さい値で更新できる場合は，更新してdequeに追加する