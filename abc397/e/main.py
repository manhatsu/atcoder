import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, K = map(int, input().split())
# A = list(map(int, input().split()))

G = [[] for _ in range(N*K)]

if N*K-1 > 0:
    for _ in range(N*K-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)

seen = [0]*N*K
seen[0] = 1

cut_times = 0

def dfs(v):
    global cut_times
    size = 1
    subtree_sizes = []
    for lv in G[v]:
        if seen[lv]:
            continue
        seen[lv] = 1
        subtree_size = dfs(lv)
        if subtree_size == -1:
            return -1
        if subtree_size > K:
            return -1
        if subtree_size == K:
            cut_times += 1
        elif subtree_size < K:
            subtree_sizes.append(subtree_size)
    if len(subtree_sizes) > 2:
        return -1
    if len(subtree_sizes) == 2:
        if sum(subtree_sizes) + 1 < K or sum(subtree_sizes) + 1 > K:
            return -1
        else:
            return K
    if len(subtree_sizes) == 1:
        size += subtree_sizes[0]
    
    return size

if dfs(0) == K and cut_times == N-1:
    print("Yes")
else:
    print("No")