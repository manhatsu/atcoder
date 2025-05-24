N, K = map(int, input().split())
# A_list = list(map(int, input().split()))

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

primes = getprimes(N)

S = [0]*(N+1)

for p in primes:
    for bp in range(p, N+1, p):
        S[bp] += 1

ans = 0
for s in S:
    if s >= K:
        ans += 1

print(ans)

