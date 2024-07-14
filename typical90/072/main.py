H, W = map(int, input().split())
# A_list = list(map(int, input().split()))

F = []

for _ in range(H):
    F.append(input())

seen = [[0]*W for _ in range(H)]

dh = [0, 1, 0, -1]
dw = [1, 0, -1, 0]

def dfs(sh, sw, ph, pw):
    if (sh == ph) and (sw == pw) and (seen[sh][sw] == 1):
        return 0
    seen[ph][pw] = 1
    ret = -100000
    for i in range(4):
        nh = ph + dh[i]
        nw = pw + dw[i]
        if (0 <= nh < H) and (0 <= nw < W):
            if (F[nh][nw] == '.'):
                if (seen[nh][nw] == 0) or ((sh == nh) and (sw == nw)):
                    v = dfs(sh, sw, nh, nw)
                    ret = max(v+1, ret)
    seen[ph][pw] = 0
    return ret

ans = -1
for h in range(H):
    for w in range(W):
        ret = dfs(h, w, h, w)
        ans = max(ans, ret)

print(ans if ans > 2 else -1)

# バックトラッキング． 要復習
