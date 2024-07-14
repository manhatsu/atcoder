N, K = map(int, input().split())
A = list(map(int, input().split()))

A = set(A)
A = [a if a <= K else 0 for a in A]
sumA = sum(set(A))

ret = int(K * (K+1)) // 2 - sum(A) # //ではなく/にすると計算おかしい

print(int(ret))