
H, W, M = map(int, input().split())

Q = []
painted_row = set()
painted_col = set()
toadd_H = H
toadd_W = W
ans = [0]*(2*(10**5)+1)
for i in range(M):
    t, a, x = map(int, input().split())
    Q.append((t, a, x))

Q = Q[::-1]

for t, a, x in Q:
    if t == 1:
        if a in painted_row:
            continue
        painted_row.add(a)
        ans[x] += toadd_W
        if toadd_H > 0:
            toadd_H -= 1
    else:
        if a in painted_col:
            continue
        painted_col.add(a)
        ans[x] += toadd_H
        if toadd_W > 0:
            toadd_W -= 1

ans[0] = H*W-sum(ans[1:])

print(sum([1 if a != 0 else 0 for a in ans]))
for i in range(len(ans)):
    if ans[i] != 0:
        print(i, ans[i])