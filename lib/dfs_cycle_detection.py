# dfsでサイクル検出
# O(N+M)
# 有向グラフのとき
# 無向グラフのときはUnion-Findが使える。有向でもUnion-Findで解ける時ある

import sys
sys.setrecursionlimit(10**6)

N = 5 # ノード数
G = [[] for i in range(N)]
# Gに辺追加しておく

# グラフ全体にサイクルがあるか
seen = [False] * N
on_stack = [False] * N

def dfs(v):
    seen[v] = True
    on_stack[v] = True
    
    for lv in G[v]:
        if on_stack[lv]:
            return False
        if not seen[lv] and not dfs(lv):
            return False
    
    on_stack[v] = False
    return True

ans = True

for i in range(N): 
    if not seen[i]:
        if not dfs(i):
            ans = False
            break
    
print('Yes' if ans else 'No')

# 特定の頂点からスタートするサイクル検出



