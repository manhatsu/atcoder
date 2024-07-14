# setrecursionlimitしておく

import sys
sys.setrecursionlimit(10**6)

# 2次元グリッド
N = int(input()) # 頂点の数

G = [[] for _ in range(N)] # 隣接グラフ
F = [] # field

H = 0
W = 0
dh = [0, 1, 0, -1]
dw = [1, 0, -1, 0]
seen = [[0]*W for _ in range(H)]
# 始点のseen=1にしておく
def dfs(h, w):
    seen[h][w] = 1
    for i in range(4):
        nexh = h+dh[i]
        nexw = w+dw[i]
        if nexh < 0 or nexh >= H or nexw < 0 or nexw >= W:
            continue
        if F[nexh][nexw] == '#':
            continue
        if seen[nexh][nexw] != 0:
            continue
        dfs(nexh, nexw)
    
# 1次元
seen = [0]*N
def dfs(v):
    seen[v] = 1
    # v から行ける各頂点 lv について
    for lv in G[v]:
        if seen[lv] != 0:
            continue # lv が探索済だったらスルー
        dfs(lv) # 再帰的に探索

        

# 1次元 stack(list)で実装
time = 0
arrive_time = [-1]*N # 行きがけ順
finish_time = [-1]*N # 帰りがけ順
# 深さ優先探索
def dfs(v):
    global time
    stack = [v]
    arrive_time[v] = time
    while stack:
        v = stack[-1]
        seenAll = True
        for lv in G[v]:
            if arrive_time[lv] < 0:
                seenAll = False
                time += 1
                arrive_time[lv] = time
                stack.append(lv) 
        if seenAll:
            time += 1
            finish_time[v] = time
            stack.pop()          
    return arrive_time, finish_time

# 孤立している頂点対策
for i in range(N):
    if arrive_time[i] < 0:
        ans = dfs(i)
