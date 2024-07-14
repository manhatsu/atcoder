H, W = map(int, input().split())

F = []

for _ in range(H):
    P = list(map(int, input().split()))
    F.append(P)

ans = 0
for i in range(2**H):
    selh = []
    for j in range(H):
        if ((i >> j) & 1):
            selh.append(j)
    cand = [0]*(H*W+1)
    if len(selh) == 0:
        continue
    for k in range(W):
        num = F[selh[0]][k]
        ret = True
        for h in selh:
            if F[h][k] != num:
                ret = False
                break
        if ret:
            cand[num] += 1
    len_selw = max(cand)
    ans = max(len(selh)*len_selw, ans)

print(ans)
            





