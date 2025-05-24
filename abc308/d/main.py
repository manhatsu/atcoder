from collections import deque

H, W = map(int, input().split())
F = []
for i in range(H):
    F.append(input())

ret = True
snuke = 'snuke'
ans = 'No'
if F[0][0] == 's':
    dw = [0, 1, 0, -1]
    dh = [1, 0, -1, 0]
    ans = 'No'
    seen = [[0]*W for i in range(H)]
    seen[0][0] = 1
    Q = deque()
    Q.append((0, 0, 0))
    while Q:
        nh, nw, d = Q.popleft()
        if nh == H-1 and nw == W-1:
            ans = 'Yes'
            break
        for i in range(4):
            nexh = nh + dh[i]
            nexw = nw + dw[i]
            if nexh < 0 or nexh >= H or nexw < 0 or nexw >= W:
                continue
            if seen[nexh][nexw]:
                continue
            if F[nexh][nexw] == snuke[(d+1)%5]:
                seen[nexh][nexw] = 1
                Q.append((nexh, nexw, (d+1)%5))

print(ans)




