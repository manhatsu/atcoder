# from collections import defaultdict, deque
# from itertools import combinations, permutations
# import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N = int(input())
# N, K = map(int, input().split())
A = list(map(int, input().split()))

if N == 1:
    ans = 1
else:

    temp = 1
    prev_val = -1
    prev_diff = -1
    continuous_num_list = []
    for i, a in enumerate(A):
        if i == 0:
            prev_val = a
            # prev_diff = a
            continue
        if i == 1:
            prev_diff = a - prev_val
            prev_val = a
            continue
        if (a - prev_val) == prev_diff:
            temp += 1
            prev_val = a
            continue
        else:
            continuous_num_list.append(temp)
            temp = 1
            prev_diff = a - prev_val
            prev_val = a

    continuous_num_list.append(temp)

    # print(continuous_num_list)

    ans = N
    for n in continuous_num_list:
        if n == 1:
            ans += 1
        else:
            ans += n*(n-1)//2+n

print(ans)
