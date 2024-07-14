import numpy as np

N = int(input())
A = []
C = []

for _ in range(N):
    a, c = map(int, input().split())
    A.append(a)
    C.append(c)

idx = list(np.arange(0, N))
# print(C)
# print(A)
# print(idx)
zip_lists = zip(C, A, idx)
zip_sort = sorted(zip_lists)
C = [x for x, _, _ in zip_sort]
A = [x for _, x, _ in zip_sort]
idx = [x for _, _, x in zip_sort]

# print(C)
# print(A)
# print(idx)
max_temp = A[0]
res = [1]*N
for i in range(1, N):
    if max_temp > A[i]:
        res[i] = 0
    else:
        max_temp = A[i]

# print(res)

res_idx = []
for i, x in enumerate(idx):
    if res[i] == 1:
        res_idx.append(x+1)

res_idx = sorted(res_idx)

print(len(res_idx))
print(*res_idx)