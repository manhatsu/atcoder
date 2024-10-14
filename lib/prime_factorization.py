# 素因数分解
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

# 最大公約数
# O(log(min(a, b)))
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
# 最小公倍数
def lcm(a, b):
    d = gcd(a, b)
    return int(a/d*b)

# エラトステネスのふるい
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