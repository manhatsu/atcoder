# H, W = map(int, input().split())
# F = []

# for i in range(H):
#     s = input()
#     F.append(s)

# dh = [1, 1, -1, -1]
# dw = [1, -1, 1, -1]

# ans = [0]*(min(H, W)+1)

# for h in range(H):
#     for w in range(W):
#         if F[h][w] != '#':
#             continue
#         flag = True
#         for i in range(4):
#             nh = h+dh[i]
#             nw = w+dw[i]
#             if not ((0 <= nh < H) and (0 <= nw < W)):
#                 flag = False
#                 break
#             if F[nh][nw] != '#':
#                 flag = False
#                 break
#         if not flag:
#             continue
#         # print('found x center:', h, w)
#         size = 1
#         while True:
#             if ((h-(size+1)) < 0) or ((w-(size+1)) < 0):
#                 break
#             if F[h-(size+1)][w-(size+1)] != '#':
#                 break
#             size += 1
#         ans[size] += 1

# print(*ans[1:])

H, W = map(int, input().split())

F = []
for _ in range(H):
    F.append(input())

def check(ch, cw):
    size = 0
    s = 1
    while True:
        if ch+s >= H or cw+s >= W or ch-s < 0 or cw-s < 0:
            break
        if F[ch+s][cw+s] == '#' and F[ch-s][cw-s] == '#' and F[ch+s][cw-s] == '#' and F[ch-s][cw+s] == '#':
            size = s
            s += 1
        else:
            break
    return size

ans = [0]*(min(H, W)+1)
for i in range(H):
    for j in range(W):
        if F[i][j] == '#':
            ans[check(i, j)] += 1

print(*ans[1:])
        








