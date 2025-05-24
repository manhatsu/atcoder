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
Q = []
for i in range(N):
    t, x = map(int, input().split())
    x -= 1
    Q.append((t, x))

isUse = [0]*N
nEnemy = [0]*N
nPortion = [0]*N

for i in range(N-1, -1, -1):
    t, x = Q[i]
    if t == 1:
        if nEnemy[x] > nPortion[x]:
            isUse[i] = 1
            nPortion[x] += 1
    else:
        nEnemy[x] += 1

ans = 0
temp_sum_portion = 0
portion_dict = defaultdict(int)
for i in range(N):
    t, x = Q[i]
    if t == 1:
        if isUse[i] == 1:
            portion_dict[x] += 1
            temp_sum_portion += 1
    else:
        portion_dict[x] -= 1
        temp_sum_portion -= 1
        if portion_dict[x] < 0:
            ans = -1
            break
    ans = max(ans, temp_sum_portion)

ans_isUse = [isUse[i] for i in range(N) if Q[i][0] == 1]

print(ans)
if ans != -1:
    print(*ans_isUse)
    

