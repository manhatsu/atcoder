N, K = map(int, input().split())
# A_list = list(map(int, input().split()))

# valが何番目に出てきたか
V = [-1]*(100000)
V[N] = 0

# i番目のval
W = [-1]*(100000)
W[0] = N

ls = -1
le = -1
for i in range(1, K+1):
    y = sum([int(s) for s in str(N)])
    N = (N+y) % 100000
    # print(N)
    if V[N] != -1:
        ls = V[N]
        le = i
        break
    V[N] = i
    W[i] = N

print(W[(K - ls) % (le-ls) + ls] if ls != -1 else N)

# 周期がiとわかる
# 周期性がある（同じ数に戻ると繰り返す）ことさえわかれば，規則性はわからずとも実装できる