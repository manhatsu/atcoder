
N, S = map(int, input().split())
A = []
B = []

for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

dp = [[0]*10001 for i in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    for j in range(10001):
        if j-A[i-1] >= 0:
            dp[i][j] |= dp[i-1][j-A[i-1]]
        if j-B[i-1] >= 0:
            dp[i][j] |= dp[i-1][j-B[i-1]]

if dp[N][S] == 1:
    ret = ''
    nowS = S
    for i in range(N-1, -1, -1):
        if dp[i][nowS-A[i]] == 1:
            ret += 'H'
            nowS -= A[i]
        elif dp[i][nowS-B[i]] == 1:
            ret += 'T'
            nowS -= B[i]
        else:
            print('Error')
    
    ret = ret[::-1]
    print('Yes')
    print(ret)
else:
    print('No')
    






