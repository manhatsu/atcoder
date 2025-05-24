import sys
sys.setrecursionlimit(4100000)
N = int(input())
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))

G = [[] for i in range(N)]

for _ in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

## 自分を含めた子ノードの数
C = [1]*N

seen = [0]*N
seen[0] = 1

def dfs(v):
    for lv in G[v]:
        if seen[lv]:
            continue
        seen[lv] = 1
        dfs(lv)
        C[v] += C[lv]

dfs(0)

ans = 0
for i in range(N):
    # 自分を含めた子ノード(C[i])からそれ以外のノード(N-C[i]までは必ず1つの辺で繋がっている。
    # この辺をまたいで移動する組み合わせの分だけその辺を使うことになる
    ans += C[i]*(N-C[i])

print(ans)




