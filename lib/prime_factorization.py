# 素因数分解
def prime_factorization(N):
    a = []
    while (N >= 2 and N % 2 == 0):
        N /= 2
        a.append(2)
    q = 3
    for i in range(int(q), int(N ** 0.5)+1, 2):
        # print(i)
        while (N % i == 0):
            N /= i
            a.append(i)
    if N > 1:
        a.append(N)

    return a

# 最大公約数
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
# 最小公倍数
def lcm(a, b):
    d = gcd(a, b)
    return int(a/d*b)