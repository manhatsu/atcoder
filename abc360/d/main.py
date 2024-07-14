
N, T = map(int, input().split())
S = input()
X = list(map(int, input().split()))

pos = []
neg = []
for i, s in enumerate(S):
    if s == '0':
        neg.append(X[i])
    else:
        pos.append(X[i])

pos = sorted(pos)
neg = sorted(neg)

pos = [p + 10**9 for p in pos]
neg = [n + 10**9 for n in neg]

def is_ok1(m, p):
    q = neg[m]
    return p >= q

def is_ok2(m, p):
    q = neg[m]
    return abs(q-p) <= T*2

def bs1(ok, ng, p): # okの初期値は-1, ngの初期値は最大idx+1
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        if is_ok1(mid, p):
            ok = mid
        else:
            ng = mid
    return ok

def bs2(ok, ng, p): # okの初期値は-1, ngの初期値は最大idx+1
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        if is_ok2(mid, p):
            ok = mid
        else:
            ng = mid
    return ok

ans = 0
for p in pos:
    # print('p', p)
    okn = bs1(-1, len(neg), p)
    # print('okn', okn)
    ok_ng = bs2(okn,len(neg), p)
    # print('ok_ng', ok_ng)
    ans += ok_ng+1 - (okn+1)
    # print('ans:', ans)

print(ans)


    
    






