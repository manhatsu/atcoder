from collections import deque
H, W = map(int, input().split())
# A_list = list(map(int, input().split()))

F = []

sh, sw = -1, -1
for i in range(H):
    F.append(input())
    for j in range(W):
        if F[i][j] == 'S':
            sh = i
            sw = j

dh = [0, 1, 0, -1]
dw = [1, 0, -1, 0]

Q = deque()

seen = [[[-1]*4 for w in range(W)] for h in range(H)]
for i in range(4):
    seen[sh][sw][i] = 0
    nexh = sh + dh[i]
    nexw = sw + dw[i]
    if nexh < 0 or nexh >= H or nexw < 0 or nexw >= W:
        continue
    if F[nexh][nexw] == '#':
        continue
    seen[nexh][nexw][i] = 1
    Q.append((nexh, nexw, i, 1))
    
ret = False

while Q and not ret:
    nh, nw, direc, val = Q.popleft()
    for i in range(4):
        nexh = nh + dh[i]
        nexw = nw + dw[i]
        if nexh < 0 or nexh >= H or nexw < 0 or nexw >= W:
            continue
        if F[nexh][nexw] == '#':
            continue
        if seen[nexh][nexw][direc] >= 0:
            continue
        for j in range(4):
            if j == direc:
                continue
            else:
                if seen[nexh][nexw][j] < 0:
                    continue
                if seen[nexh][nexw][j] + val + 1 >= 4:
                    ret = True
                    break
        if ret:
            break

        seen[nexh][nexw][direc] = val+1
        Q.append((nexh, nexw, direc, val+1))

print('Yes' if ret else 'No')








