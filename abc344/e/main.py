
N = int(input())
# N, K = map(int, input().split())
A = list(map(int, input().split()))

A = [0]+A+[-1]

mae = [None]+[A[i-1] for i in range(1, len(A))]
ushiro = [A[i+1] for i in range(0, len(A)-1)]+[None]

val2idx = dict()
for i in range(len(A)):
    val2idx[A[i]] = i

def insert(x, y):
    x_idx = val2idx[x]
    z = ushiro[x_idx]
    if z is not None:
        z_idx = val2idx[z]
        mae[z_idx] = y
    val2idx[y] = len(mae)
    ushiro[x_idx] = y
    ushiro.append(z)
    mae.append(x)

def delete(x):
    x_idx = val2idx[x]
    w = mae[x_idx]
    y = ushiro[x_idx]
    if w is not None:
        w_idx = val2idx[w]
        ushiro[w_idx] = y
    if y is not None:
        y_idx = val2idx[y]
        mae[y_idx] = w 
    del val2idx[x]

Q = int(input())
for i in range(Q):
    l = list(map(int, input().split()))
    if l[0] == 1:
        insert(l[1], l[2])
    else:
        delete(l[1])

ans = []
v = 0
while v != -1:
    ans.append(v)
    idx = val2idx[v]
    v = ushiro[idx]

print(*ans[1:]) 





