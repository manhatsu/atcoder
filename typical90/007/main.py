N = int(input())
# N, K = map(int, input().split())
A = list(map(int, input().split()))
Q = int(input())
B = []
b_idx = [i for i in range(Q)]
for _ in range(Q):
    B.append(int(input()))

A = sorted(A)

zip_b = zip(B, b_idx)
s_zip= sorted(zip_b)
B, b_idx = zip(*s_zip)
B = list(B)
b_idx = list(b_idx)

ret = []
i = 0
j = 0
flag = False
while (i < N) and (j < Q):
    while (A[i] < B[j]):
        i += 1
        if i >= N:
            flag = True
            break
    if flag:
        break
    if i == 0:
        ret.append(A[i]-B[j])
    else:
        ret.append(min(abs(A[i]-B[j]), abs(A[i-1]-B[j])))
    j += 1

if len(ret) < Q:
    for k in range(j, Q):
        ret.append(abs(A[N-1]-B[k]))

# print(len(ret))

zip_r = zip(b_idx, ret)
s_zip_r = sorted(zip_r)
b_idx, ret = zip(*s_zip_r)

for i in range(Q):
    print(ret[i])