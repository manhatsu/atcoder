N = int(input())
S = input()
C = list(map(int, input().split()))

# 累積和
D0 = [] # 010101...にするためのコスト
D1 = [] # 101010...にするためのコスト
e = [0, 1]
# temp
d0 = 0
d1 = 0
for i in range(N):
    # print('S[i]', S[i], 'e[i%2]', e[i%2])
    # S[i]はstr
    if int(S[i]) == e[i%2]:
        d1 += C[i]
    else:
        d0 += C[i]
    D0.append(d0)
    D1.append(d1)

# print(D0)
# print(D1)

# 0始まり，1始まりそれぞれで，コスト最小となる切り替え点（0か1が連続する場所）を求める
inf = 10**20
ans = inf

for k in range(1, N):
    # 0始まり
    if D0[k-1]+D1[N-1]-D1[k-1] < ans:
        ans = D0[k-1]+D1[N-1]-D1[k-1]
    # 1始まり
    if D1[k-1]+D0[N-1]-D0[k-1] < ans:
        ans = D1[k-1]+D0[N-1]-D0[k-1]

print(ans)




