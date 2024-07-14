from collections import deque

H, W = map(int, input().split())
# A_list = list(map(int, input().split()))
INF = 10**9

sh, sw, gh, gw = 0, 0, 0, 0

F = []
for i in range(H):
    S = input()
    F.append(S)
    for j, s in enumerate(S):
        if s == 'S':
            sh = i
            sw = j
        if s == 'T':
            gh = i
            gw = j

# print('sh, sw', sh, sw)

E = [[0]*W for _ in range(H)]
N = int(input())
for _ in range(N):
    r, c, e = map(int, input().split())
    E[r-1][c-1] = e

DP = [[-INF]*W for _ in range(H)] # その地点における最大エネルギー
DP[sh][sw] = 0

dh = [0, 1, 0, -1]
dw = [1, 0, -1, 0]
ans = False

Q = deque()
Q.append((sh, sw))
while Q:
    h, w = Q.popleft()
    if DP[h][w] < E[h][w]: # 薬を使う
        DP[h][w] = E[h][w]
        E[h][w] = 0
    nd = DP[h][w]
    if nd <= 0:
        # もう移動できない
        continue
    for i in range(4):
        nh = h+dh[i]
        nw = w+dw[i]
        if not(0<=nh<H and 0<=nw<W) or F[nh][nw] == '#':
            continue
        if F[nh][nw] == 'T':
            if nd-1 >= 0:
                ans = True
                break
        # 値が更新される場合queに入れる
        if DP[nh][nw] < nd-1:
            DP[nh][nw] = nd-1
            Q.append((nh, nw))

print('Yes' if ans else 'No')









