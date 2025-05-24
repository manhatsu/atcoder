N, P, K = map(int, input().split())
# A_list = list(map(int, input().split()))
# from icecream import ic
# ic.disable()

A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

def F(x):
    d = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][j] == -1:
                d[i][j] = x
            else:
                d[i][j] = A[i][j]
    for k in range(N): # 経由する点
        for i in range(N): # 始点
            for j in range(N): # 終点
                d[i][j] = min(d[i][k]+d[k][j], d[i][j])
    ret = 0
    for i in range(N):
        # if N < 5:
            # ic(d[i])
        for j in range(i+1, N):
            if d[i][j] <= P:
                ret += 1
    # ic(x, ret)
    return ret

def isOK1(x):
    return F(x) > K

def isOK2(x):
    return F(x) >= K

def bs1(ok, ng):
    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        if isOK1(mid):
            ok = mid
        else:
            ng = mid
    return ok

def bs2(ok, ng):
    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        if isOK2(mid):
            ok = mid
        else:
            ng = mid
    return ok

ret1 = bs1(0, P+2)
# ic(ret1)
ret2 = bs2(0, P+2)
# ic(ret2)

if ret1 == P+1 and ret2 == P+1:
    print(0)
elif ret2 == P+1:
    print("Infinity")
else:
    print(ret2-ret1)