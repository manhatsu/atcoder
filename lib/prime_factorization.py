# 素因数分解 O(√N)
def prime_factorization(N):
    a = []
    cnt = 0
    while (N >= 2 and N % 2 == 0):
        N //= 2
        cnt += 1
    if cnt > 0:
        a.append([2, cnt])
    q = 3
    for i in range(int(q), int(N ** 0.5)+1, 2):
        cnt = 0
        while (N % i == 0):
            N //= i
            cnt += 1
        if cnt > 0:
            a.append([i, cnt])
    if N > 1:
        a.append([N, 1])
    return a

# 約数列挙 O(√N)
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

# 素数列挙 O(NloglogN) つまり、素数の個数はloglogN個
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


# 素数列挙を使い、N以下の数に対して素因数の個数を列挙 O(NloglogN)

N = 5 # sample

primes = getprimes(N)
S = [0]*(N+1)

for p in primes:
    for bp in range(p, N+1, p):
        S[bp] += 1