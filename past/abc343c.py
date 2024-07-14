H, W, N = map(int, input().split())
T = input()
Tidx = []

D = {'R':0, 'U':1, 'L':2, 'D':3}
for t in T:
    Tidx.append(D[t])

# print(Tidx)


F = [[] for _ in range(H)]
for i in range(H):
    S = [s for s in input()]
    F[i] = S

# R, U, L, D
dw = [1, 0, -1, 0]
dh = [0, -1, 0, 1]

ret = 0
for h in range(H):
    for w in range(W):
        nowh = h
        noww = w
        # print('start from', nowh, noww)
        if F[nowh][noww] == '#':
            continue
        flag = 0
        for t in Tidx:
            nowh += dh[t]
            noww += dw[t]
            # print('nowh, noww', nowh, noww)
            if (0 <= nowh < H) and (0 <= noww < W):
                if F[nowh][noww] == '.':
                    continue
                else:
                    flag = 1
                    break
            else:
                flag = 1
                break
        if flag:
            # print('failed')
            continue
        # print('ok')
        ret += 1
            
print(ret)

