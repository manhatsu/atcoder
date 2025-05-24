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