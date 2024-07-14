N, T = map(int, input().split())
A = list(map(int, input().split()))

def toIJ(num):
    i = (num-1) // N
    j = (num-1) % N
    return i, j

i_b = [0]*N
j_b = [0]*N
s_b = [0]*2

ret = -1
for turn, a in enumerate(A):
    i, j = toIJ(a)
    if i == j:
        s_b[0] += 1
        if s_b[0] == N:
            ret = turn
            break
    if i+j == N-1:
        s_b[1] += 1
        if s_b[1] == N:
            ret = turn
            break
    i_b[i] += 1
    j_b[j] += 1
    if i_b[i] == N or j_b[j] == N:
        ret = turn
        break

print(ret+1 if ret != -1 else -1)
    
