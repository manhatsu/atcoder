N, T = input().split()
N = int(N)

def isPossible(S, T): # 長さS >= T前提
    if len(S) < len(T):
        return isPossible(T, S)
    A = 0
    miss = 0
    if len(S) - len(T) > 1:
        return False
    if len(S) == len(T):
        for i in range(len(T)):
            if S[i] != T[i]:
                miss += 1
            if miss > 1:
                return False
        return True
    else:
        for i in range(len(T)):
            if S[i+miss] != T[i]:
                miss += 1
                if S[i+1] == T[i]:
                    continue
                else:
                    return False
            if miss > 1:
                return False
        return True

ret = []  
for i in range(N):
    if isPossible(input(), T):
        ret.append(i+1)

print(len(ret))
print(*ret)

'''
# 以下TLE
from functools import lru_cache

@lru_cache(maxsize=None)
def ld(s, t):
    if not s:
        return len(t)
    if not t:
        return len(s)
    
    if s[0] == t[0]:
        return ld(s[1:], t[1:])
    
    left = ld(s[1:], t)
    upp = ld(s, t[1:])
    lupp = ld(s[1:], t[1:])

    return 1 + min(left, upp, lupp)

ret = []
for i in range(N):
    S = input()
    D = ld(S, T)
    if (D <= 1):
        ret.append(i+1)

print(len(ret))
print(*ret)

'''