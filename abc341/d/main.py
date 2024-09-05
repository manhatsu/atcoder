# from collections import defaultdict, deque
# from itertools import combinations, permutations
import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

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

# binary search
def is_ok(mid):
    return mid+mid*N//M <= L

def binary_search(ok, ng): # okの初期値は-1, ngの初期値は最大idx+1
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

N, M, K = map(int, input().split())

LCM = lcm(N, M)
# print('LCM', LCM)

Q = LCM//N-1+LCM//M-1 # LCMおきにQ個出てくる
# print('Q', Q)
J = K//Q
# print('J', J)
L = K%Q # 残り
# print('L', L)
if L == 0:
    ans = J*LCM-min(N, M)
else:
    alpha = binary_search(0, LCM//N)
    # print('alpha', alpha)
    beta = L - (alpha+alpha*N//M)
    if beta == 0:
        ans = J*LCM+alpha*N
    else:
        ans = J*LCM+math.ceil(alpha*N/M)*M+(beta-1)*M

print(ans)

