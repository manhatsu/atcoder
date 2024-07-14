N = int(input())
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))
L = []
R = []
minimum = 0
yuuyo = 0
for i in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
    minimum += l
    yuuyo += (r-l)

ans = False
if minimum == 0:
    ans = True
elif minimum < 0:
    if yuuyo + minimum >= 0:
        ans = True
summ = minimum
if ans:
    ret_list = []
    for i in range(N):
        if summ == 0:
            ret_list.append(L[i])
        elif summ < 0:
            if (-summ) < (R[i]-L[i]):
                ret_list.append(L[i]+(-summ))
                summ = 0
            else:
                ret_list.append(R[i])
                summ += R[i]-L[i]
        else:
            raise ValueError
            

if ans:
    print('Yes')
    print(*ret_list)
else:
    print('No')




