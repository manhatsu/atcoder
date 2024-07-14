
N = int(input())
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))

def ndivisors(M):
    ret = 0
    for i in range(1, int(M**0.5)+1):
        if M%i == 0:
            ret += 1
            if i != M//i:
                ret += 1
    return ret

D = [0]
for i in range(1, N):
    D.append(ndivisors(i))

ans = 0
for i in range(1, N):
    ans += D[i]*D[N-i]

print(ans)



