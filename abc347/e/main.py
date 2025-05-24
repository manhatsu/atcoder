N, Q = map(int, input().split())
X = list(map(int, input().split()))

A = [0]*(N+1)

S = set()
T = [0]*(Q+1) # |S|の累積和
added_idx = [-1]*(N+1)

for i in range(Q):
    if X[i] not in S:
        S.add(X[i])
        added_idx[X[i]] = i
    else:
        S.remove(X[i])
        A[X[i]] += T[i] - T[added_idx[X[i]]]
        added_idx[X[i]] = -1
    T[i+1] = T[i]+len(S)
    # print(*A)

# print('T', *T)
# print(*A)
# print('added_idx', *added_idx)
for i, a in enumerate(added_idx[1:], start=1):
    if a != -1:
        A[i] += T[Q] - T[a]

print(*A[1:])