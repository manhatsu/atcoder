
N = int(input())
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))

S = []

for i in range(N):
    S.append((input(), i))

S = sorted(S, key=lambda x:x[0])

L = [0]*N

for j in range(N-1):
    # print('j', j)
    iter = min(len(S[j][0]), len(S[j+1][0]))
    # print('iter', iter)
    lcp = 0
    for k in range(iter):
        if S[j][0][k] != S[j+1][0][k]:
            break
        lcp += 1
    # print('lcp', lcp)
    L[j] = max(L[j], lcp)
    L[j+1] = max(L[j+1], lcp)

ans = [0]*N
for i in range(N):
    idx = S[i][1]
    ans[idx] = L[i]

for i in range(N):
    print(ans[i])
    