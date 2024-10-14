N = int(input())
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))
from bisect import bisect, bisect_left, bisect_right

def getprimes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

primes = getprimes(10**6)

ans = 0
for i, a in enumerate(primes):
    if a >= 10**3:
        break
    temp = a**2
    for j, b in enumerate(primes[i+1:], start=i+1):
        if b >= 10**4:
            break
        temp2 = temp*b
        if temp2 >= N:
            break
        limit = int((N // temp2)**0.5)
        limit_pos = bisect_right(primes, limit)
        ans += max(0, limit_pos - (j + 1))

print(ans)





