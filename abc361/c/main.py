N, K = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A)

# 最小の差を保存する変数を大きな値で初期化
min_diff = float('inf')

# 両端から削る個数を調整しながら最小差を求める
for i in range(K+1):
    min_element = A[i]
    max_element = A[N-K+i-1]
    min_diff = min(min_diff, max_element - min_element)

print(min_diff)





