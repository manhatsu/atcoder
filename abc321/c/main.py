K = int(input())
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))

import math

def NCM(N, M):
    return math.factorial(N) // (math.factorial(M) * math.factorial(N-M))

S = [0]
temp = 0
for i in range(1, 11):
    if i == 1:
        temp += 9
    else:
        # 先頭0はなし
        temp += NCM(10, i)
    S.append(temp)

# print(S)

def isOK(m):
    return S[m] < K

def bsearch(l, r):
    if abs(l-r) <= 1:
        return l
    mid = (l+r) // 2
    if isOK(mid):
        l = mid
    else:
        r = mid
    return(bsearch(l, r))

digit = bsearch(0, len(S)+1) + 1
# print('digit:', digit)

if digit == 1:
    ans = K

else:
    import itertools
    J = K - S[digit-1]
    comb_list = list(itertools.combinations([i for i in range(10)], digit))
    cand = []
    for c in comb_list:
        s = ''
        for l in c[::-1]:
            s += str(l)
        cand.append(int(s))

    cand = sorted(cand)
    ans = cand[J-1]

print(ans)


