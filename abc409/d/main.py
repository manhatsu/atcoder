from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys

sys.set_int_max_str_digits(10000000)
sys.setrecursionlimit(4100000)
import heapq
try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

T = int(input())

def solve(S):
    start = -1
    for i in range(len(S)-1):
        if ord(S[i]) > ord(S[i+1]):
            start = i
            break
    if start == -1:
        return S
    
    for k in range(start+1, len(S)):
        end = len(S)
        if ord(S[k]) > ord(S[start]):
            end = k
            break

    # ic(start, end)

    T = []
    for i in range(start):
        T.append(S[i])
    # ic(T)
    for i in range(start+1, end):
        T.append(S[i])
    # ic(T)
    T.append(S[start])
    # ic(T)
    for i in range(end, len(S)):
        T.append(S[i])
    # ic(T)
    return "".join(T)

for _ in range(T):
    N = int(input())
    S = input()
    ans = solve(S)
    print(ans)