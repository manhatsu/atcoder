
N = int(input())
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

dp = [False] * (2**N)

for i in range(2**N):
    if dp[i] == True:
        continue
    for j in range(N-1):
        for k in range(j+1, N):
            if A[j] == A[k] or B[j] == B[k]:
                if not(i >> j & 1) and not (i >> k & 1):
                    dp[i | 2**j | 2**k] = True

if dp[2**N-1]:
    print('Takahashi')
else:
    print('Aoki')
    



