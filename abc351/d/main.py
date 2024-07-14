H, W = map(int, input().split())
import sys
sys.setrecursionlimit(10**8)
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))
from collections import deque
# A_list = list(map(int, input().split()))

F = []
for _ in range(H):
    F.append(input())

seen = [[0]*W for _ in range(H)]

dh = [0, 1, 0, -1]
dw = [1, 0, -1, 0]

# 磁石に隣接するマスのフラグ
isAdj = [[0]*W for i in range(H)]
for w in range(W):
    for h in range(H):
        if F[h][w] == '#':
            for i in range(4):
                nh = h+dh[i]
                nw = w+dw[i]
                if (nh<0) or (nh>=H) or (nw<0) or (nw>=W):
                    continue
                isAdj[nh][nw] = 1

# dfsだとTLE. bfsならAC
# 既に通った磁石に隣接するマスをseen_adj (set) で管理する
# seen_adjに入っているときには+1しない
def dfs(h, w):
    global v
    global seen_adj
    # print('start dfs', h, w)
    # print('seen adj', *seen_adj)
    if (seen[h][w]!=0) or ((h, w) in seen_adj):
        # print('already seen')
        return
    v += 1
    # print('v', v)
    if isAdj[h][w]:
        # print('add {}, {} to seen adj'.format(h, w))
        seen_adj.add((h, w))
        return v
    seen[h][w] = 1
    # search = True
    # for i in range(4):
        # nh = h+dh[i]
        # nw = w+dw[i]
        # if (nh<0) or (nh>=H) or (nw<0) or (nw>=W):
            # continue
        # if F[nh][nw] == '#':
            # search = False
            # break
    # if not search:
        # seen[h][w] = 0
        # return
    # print('search adjacent pixels')
    for i in range(4):
        nh = h+dh[i]
        nw = w+dw[i]
        if (nh<0) or (nh>=H) or (nw<0) or (nw>=W):
            continue
        if (F[nh][nw] == '#') or (seen[nh][nw] != 0):
            continue
        dfs(nh, nw)
    return v

ans = 1
for h in range(H):
    for w in range(W):
        if (seen[h][w] != 0) or (F[h][w] == '#') or (isAdj[h][w]):
            continue
        v = 0
        seen_adj = set()
        Q = deque()
        Q.append((h, w))
        while Q:
            nh, nw = Q.popleft()
            if seen[nh][nw] or (nh, nw) in seen_adj:
                continue
            v += 1
            if isAdj[nh][nw]:
                seen_adj.add((nh, nw))
                continue
            seen[nh][nw] = 1
            for i in range(4):
                nexh = nh + dh[i]
                nexw = nw + dw[i]
                if not(0<=nexh<H and 0<=nexw<W) or F[nexh][nexw] == '#' or seen[nexh][nexw]:
                    continue
                Q.append((nexh, nexw))
        
        # dfs(h, w)
        if v > ans:
            # print('ans updated to', v)
            ans = v
print(ans)