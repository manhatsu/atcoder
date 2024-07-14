N, M, H, K = map(int, input().split())
# A_list = list(map(int, input().split()))
S = input()

# F = [[0]*(4*10**5+1) for i in range(4*10**5+1)]
D = {}

for _ in range(M):
    w, h = map(int, input().split())
    # F[x+2*10**5][y+2*10**5] = 1
    D[(h+2*10**5, w+2*10**5)] = 1

# print(D)

# r, l, u, d
dic = {'R':0, 'L':1, 'U':2, 'D':3}
dh = [0, 0, 1, -1]
dw = [1, -1, 0, 0]

nh = 2*10**5
nw = 2*10**5

ans = True
for s in S:
    idx = dic[s]
    nh = nh+dh[idx]
    nw = nw+dw[idx]
    # print('now:', nh, nw)
    H -= 1
    # print('H:', H)
    if H < 0:
        ans = False
        break
    if (nh, nw) in D.keys():
        if H < K:
            H = K
            del D[(nh, nw)]

print('Yes' if ans else 'No')









