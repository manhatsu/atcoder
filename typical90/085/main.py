K = int(input())
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))

def getHalfDivisorList(N): # O(sqrt(N))
    ans = []
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            ans.append(i)
            # if (i*i != N):
                # ans.append(N // i)
    ans = sorted(ans)
    return ans

A = getHalfDivisorList(K)

ret = 0
ret_trios = []
for i, a in enumerate(A):
    L = K // a
    for b in A[i:]:
        if L % b == 0:
            if b <= L // b:
                ret += 1
                # ret_trios.append((a, b, L//b))
print(ret)
# for i in range(len(ret_trios)):
    # print(ret_trios[i])