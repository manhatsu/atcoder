A, B, C = map(int, input().split())

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

d = gcd(A, B)
e = gcd(A, C)

G = gcd(d, e)

a, b, c = [i // G for i in (A, B, C)]

print(a+b+c-3)



