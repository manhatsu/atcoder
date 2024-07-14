H, W = map(int, input().split())
F = []

for i in range(H):
    s = input()
    F.append(s)

dh = [1, 1, -1, -1]
dw = [1, -1, 1, -1]

ans = [0]*(min(H, W)+1)

for h in range(H):
    for w in range(W):
        if F[h][w] != '#':
            continue
        flag = True
        for i in range(4):
            nh = h+dh[i]
            nw = w+dw[i]
            if not ((0 <= nh < H) and (0 <= nw < W)):
                flag = False
                break
            if F[nh][nw] != '#':
                flag = False
                break
        if not flag:
            continue
        # print('found x center:', h, w)
        size = 1
        while True:
            if ((h-(size+1)) < 0) or ((w-(size+1)) < 0):
                break
            if F[h-(size+1)][w-(size+1)] != '#':
                break
            size += 1
        ans[size] += 1

print(*ans[1:])
        








