H, W = map(int, input().split())
# A_list = list(map(int, input().split()))

from collections import deque

F = []
for i in range(H):
    F.append(input())

G = [[[0]*4 for i in range(W)] for j in range(H)]

arrow_dic = {'v':0, '>':1, '^':2, '<':3}

for i in range(H):
    for j in range(W):
        if F[i][j] == 'S':
            sh, sw = i, j
            continue
        if F[i][j] == 'G':
            gh, gw = i, j
            continue
        if F[i][j] == '#':
            for k in range(4):
                G[i][j][k] = 2
            continue
        if F[i][j] != '.':
            G[i][j][arrow_dic[F[i][j]]] = 1
            continue
        if i > 0 and G[i-1][j][0] == 1:
            G[i][j][0] = 1
        if j > 0 and G[i][j-1][1] == 1:
            G[i][j][1] = 1

for i in range(H-1, -1, -1):
    for j in range(W-1, -1, -1):
        if F[i][j] == 'S' or F[i][j] == 'G':
            continue
        if F[i][j] == '#' or F[i][j] != '.':
            continue
        if i < H-1 and G[i+1][j][2] == 1:
            G[i][j][2] = 1
        if j < W-1 and G[i][j+1][3] == 1:
            G[i][j][3] = 1


F = [['.']*W for i in range(H)]
for i in range(H):
    for j in range(W):
        if any(G[i][j]):
            F[i][j] = '#'

seen = [[0]*W for i in range(H)]
Q = deque()
Q.append((sh, sw, 0))
seen[sh][sw] = 1

dh = [1, 0, -1, 0]
dw = [0, 1, 0, -1]

# for i in range(H):
    # print(*F[i])

ans = -1
while Q:
    nh, nw, temp_ans = Q.popleft()
    if nh == gh and nw == gw:
        ans = temp_ans
        break
    for i in range(4):
        nexh = nh + dh[i]
        nexw = nw + dw[i]
        if nexh < 0 or nexh >= H or nexw < 0 or nexw >= W:
            continue
        if seen[nexh][nexw]:
            continue
        if F[nexh][nexw] == '#':
            continue
        seen[nexh][nexw] = 1
        Q.append((nexh, nexw, temp_ans+1))

print(ans)