from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

T = int(input())
# N, K = map(int, input().split())

def isOK(a, s):
    if a.bit_length() > s.bit_length():
        return False
    kuriagari = 0
    for i in range(s.bit_length()+1):
        if a & (1 << i):
            if kuriagari == 0:
                if s & (1 << i):
                    return False
                kuriagari = 1
            else:
                if not s & (1 << i):
                    return False
        else:
            if kuriagari == 0:
                continue
            else:
                if s & (1 << i):
                    kuriagari = 0
                else:
                    kuriagari = 1
    if kuriagari == 1:
        return False
    return True

for _ in range(T):
    a, s = map(int, input().split())
    if isOK(a, s):
        print("Yes")
    else:
        print("No")