
N = int(input())
C = list(input().split())
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))
import sys
sys.setrecursionlimit(10**6)

MOD = 10**9+7

G = [[] for _ in range(N)]

for _ in range(N-1):
    A, B = map(int, input().split())
    G[A-1].append(B-1)
    G[B-1].append(A-1)

dp = [[0]*3 for i in range(N)]
seen = [0]*N
seen[0] = 1

def dfs(v):
    temp0 = 1
    temp2 = 1
 
    for nv in G[v]:
        if seen[nv]:
            continue
        seen[nv] = 1
        dfs(nv)
        if C[v] == 'a':
            temp0 *= dp[nv][0] + dp[nv][2]
            temp2 *= dp[nv][0] + dp[nv][1] + 2 * dp[nv][2]
        else:
            temp0 *= dp[nv][1] + dp[nv][2]
            temp2 *= dp[nv][0] + dp[nv][1] + 2 * dp[nv][2]

        temp0 %= MOD
        temp2 %= MOD
    
    if C[v] == 'a':
        dp[v][0] = temp0
        dp[v][2] = (temp2 - temp0)%MOD
    else:
        dp[v][1] = temp0
        dp[v][2] = (temp2 - temp0)%MOD

dfs(0)

print(dp[0][2])




