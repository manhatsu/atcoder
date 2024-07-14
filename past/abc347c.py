N, A, B = map(int, input().split())
D = list(map(int, input().split()))
D_mod = [d % (A+B) for d in D]

D_mod = sorted(D_mod)
D_mod_week2 = [d+A+B for d in D_mod]
# print(D_mod_week2)

D_D = D_mod + D_mod_week2
# print(D_D)

ret = 'No'
for i in range(len(D_mod)):
    l = D_D[i]
    r = D_D[i+N-1]
    if r-l+1 <= A:
        ret = 'Yes'
        break

print(ret)

