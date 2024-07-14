N = int(input())
A = list(map(int, input().split()))

d = {i+1: A[i] for i in range(N)}
e = {A[i]: i+1 for i in range(N)}

ret_l = []
ret_r = []

count = 0
for i in range(1, N+1):
    if d[i] != i:
        count += 1
        ret_l.append(i)
        ret_r.append(e[i])

        d[e[i]] = d[i]
        e[d[i]] = e[i]
        d[i] = i
        e[i] = i

print(count)
if count > 0:
    for i in range(count):
        print(ret_l[i], ret_r[i])
    
        
