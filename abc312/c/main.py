import sys
sys.setrecursionlimit(10**8)

N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

'''
ans = 0
i = 0 # 売り手
j = 0 # 買い手
found = False
while (i < N) and (j < M):
    while (A[i] > B[j]):
        j += 1
        # print('x', i, M-j)
        if i >= (M-j):
            ans = B[j-1]+1
            break
    if ans:
        break
    i += 1
    # print('y', i, M-j)
    if i >= (M-j):
        ans = A[i-1]
        break
if (i == N) and (ans == 0):
    ans = B[M-N-1]+1
print(ans)
'''
        
# 二分探索での解法

def isOK(x):
    na = 0
    nb = 0
    for a in A:
        if a <= x:
            na += 1
    for b in B:
        if b >= x:
            nb += 1
    return(na < nb)
    
def bs(l, r):
    # print('bs', l, r)
    if abs(l-r)<=1:
        return l
    mid = (l+r) // 2
    if isOK(mid):
        return bs(mid, r)
    else:
        return bs(l, mid)
    
ans = bs(0, B[-1]+2)

print(ans+1)



