N, A, B = map(int, input().split())
S = input()

S = list(S)

inf = (10**9)*10**5
ans = inf

if N == 1:
    ans = 0
else:
    for i in range(len(S)):
        temp = 0
        if i == 0:
            T = S.copy()
        else:
            temp += A*i
            T = S[i:]+S[:i]
        U = T[::-1]
        for j in range(N//2):
            if T[j] != U[j]:
                temp += B
        if temp < ans:
            ans = temp

print(ans)





