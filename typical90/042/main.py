K = int(input())
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))

if K % 9 != 0:
    # print('K is not a multiple of 9')
    ans = 0
else:
    dp = [0]*(K+1)
    dp[0] = 1
    for i in range(1, K+1):
        for j in range(1, min(9, i)+1):
            dp[i] += dp[i-j]
    ans = dp[K]

print(ans % (10**9+7))




