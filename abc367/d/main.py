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

N, M = map(int, input().split())
A = list(map(int, input().split()))
AA = A+A

# 始点からかかる時間のあまりを配列として取得
temp = 0
R = [0]
for a in AA[:-1]:
    temp = (temp+a)%M
    R.append(temp)

# print(R)
B = [0]*M
for r in R[:N]:
    B[r] += 1
# print(B)

ans = 0
for i in range(N):
    # idx = i+1~i+N-1までの中でRidx == Riとなるものが何個あるか探す
    B[R[i]] -= 1
    # print(B)
    ans += B[R[i]]
    # print('ans', ans)
    B[R[N+i]] += 1

print(ans)