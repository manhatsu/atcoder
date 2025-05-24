N, S = map(int, input().split())
# A_list = list(map(int, input().split()))

ans = []
D = []
sougaku = 0
for i in range(N):
    a, b = map(int, input().split())
    if a <= b:
        ans.append('A')
        sougaku += a
        D.append(b-a)
    else:
        ans.append('B')
        sougaku += b
        D.append(a-b)

diff = S - sougaku
if diff < 0:
    print('Impossible')
    exit()

if diff == 0:
    print(''.join(ans))
    exit()

dp = [[False]*(diff+1) for _ in range(N+1)]
dp[0][0] = True

for i in range(1, N+1):
    for j in range(diff+1):
        if dp[i-1][j]:
            dp[i][j] = True
            if j+D[i-1] <= diff:
                dp[i][j+D[i-1]] = True

if dp[N][diff]:
    for i in reversed(range(N)):
        if diff-D[i] >= 0 and dp[i][diff-D[i]]:
            diff -= D[i]
            if ans[i] == 'A':
                ans[i] = 'B'
            else:
                ans[i] = 'A'

    print(''.join(ans))
else:
    print('Impossible')

