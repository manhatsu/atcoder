# from collections import defaultdict, deque
from itertools import combinations, permutations
from more_itertools import *
# import math
# import sys
# sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
# from bisect import bisect, bisect_left, bisect_right
# from collections import defaultdict, deque
# MOD = 998244353
# INF = float("inf")
# MINF = -float("inf")

N, K = map(int, input().split())
S = input()
list_S = list(S)

# perms = set((permutations(list_S)))
# itertools.permutationsでsetとると間に合わない。
# more_itertools.distinct_permutationsだとギリ間に合う
perms = distinct_permutations(list_S)

# print(perms)

def containPalindrome(S, K):
    ret = False
    for i in range(len(S)-K+1):            
        subS = S[i:i+K]
        if subS == subS[::-1]:
            ret = True
            break
    return ret

ans = 0
for T in perms:
    if containPalindrome(T, K):
        continue
    ans += 1

print(ans)
    
