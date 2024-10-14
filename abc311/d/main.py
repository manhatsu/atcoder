from collections import deque
N, M = map(int, input().split())
# A_list = list(map(int, input().split()))

F = []
for i in range(N):
    F.append(input())

sh, sw = 1, 1
dh = [0, 1, 0, -1]
dw = [1, 0, -1, 0]

seen = [[[0]*4 for i in range(M)] for j in range(N)]

Q = deque()
for i in range(4):
    Q.append((sh, sw, i))

while Q:
    nh, nw, d = Q.popleft()
    seen[nh][nw][d] = 1
    nexh = nh+dh[d]
    nexw = nw+dw[d]
    if nexh < 0 or nexh >= N or nexw < 0 or nexw >= M:
        continue
    if F[nexh][nexw] == '#':
        if not seen[nexh][nexw][d]:
            seen[nexh][nexw][d] = 1 # ここのチェックを忘れるとTLE
            for k in range(4):
                if k%2 == d%2:
                    continue
                if not seen[nh][nw][k]:
                    Q.append((nh, nw, k))
    else:
        if not seen[nexh][nexw][d]:
            Q.append((nexh, nexw, d))

ans = 0
for h in range(N):
    for w in range(M):
        if F[h][w] == '#':
            continue
        for i in range(4):
            if seen[h][w][i] == 1:
                ans += 1
                break

print(ans)



