N, K = map(int, input().split())
# A_list = list(map(int, input().split()))

MAX = 5000

F = [[0]*(MAX+1) for _ in range(MAX+1)]

for _ in range(N):
    a, b = map(int, input().split())
    F[a][b] += 1

S = [[0]*(MAX+1) for _ in range(MAX+1)]

for i in range(1, MAX+1):
    for j in range(1, MAX+1):
        S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + F[i][j]

ans = 0
for i in range(MAX+1):
    for j in range(MAX+1):
        if i+K+1 <= MAX and j+K+1 <= MAX:
            ans = max(ans, S[i+K+1][j+K+1] - S[i][j+K+1] - S[i+K+1][j] + S[i][j])

print(ans)
