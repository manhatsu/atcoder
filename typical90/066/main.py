
N = int(input())
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))
L = []
R = []

for _ in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

ans = 0

for i in range(N):
    for j in range(i+1, N):
        M = (R[i] - L[i] + 1) * (R[j] - L[j] + 1)
        C = 0
        for val in range(L[i], R[i]+1):
            if val > R[j]:
                C += R[j] - L[j] + 1
            elif val > L[j]:
                C += val - L[j]
        ans += C/M

print(ans)

################################
# 和の期待値は期待値の和
# 各ありうるi, jで期待値を求めればよい
################################




