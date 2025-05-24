H, W = map(int, input().split())
# A_list = list(map(int, input().split()))

F = []

for _ in range(H):
    F.append(input())

seen = [[0]*W for _ in range(H)]

dh = [0, 1, 0, -1]
dw = [1, 0, -1, 0]

ret = -1

def dfs2(sh, sw, nh, nw, dist):
    global ret
    if sh == nh and sw == nw and seen[nh][nw] == 1:
        ret = max(ret, dist)
        return
    seen[nh][nw] = 1
    for i in range(4):
        nnh = nh + dh[i]
        nnw = nw + dw[i]
        if (0 <= nnh < H) and (0 <= nnw < W):
            if (F[nnh][nnw] == '.'):
                if (seen[nnh][nnw] == 0) or (sh == nnh and sw == nnw):
                    dfs2(sh, sw, nnh, nnw, dist+1)
    seen[nh][nw] = 0

for h in range(H):
    for w in range(W):
        dfs2(h, w, h, w, 0)

print(ret if ret > 2 else -1)