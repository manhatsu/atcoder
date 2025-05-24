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

K = int(input())
S = input()
T = input()
# N, K = map(int, input().split())

nokori_maisuu = [K]*10
nokori_maisuu[0] = 0

aoki_maisuu = [0]*10
takahasi_maisuu = [0]*10

for s in S[:4]:
    takahasi_maisuu[int(s)] += 1
    nokori_maisuu[int(s)] -= 1

for t in T[:4]:
    aoki_maisuu[int(s)] += 1
    nokori_maisuu[int(s)] -= 1

ans = 0
aoki_kakuritu = [n / sum(nokori_maisuu) for n in nokori_maisuu]
for i in range(1, 10):
    if nokori_maisuu[i] == 0:
        continue
    temp_nokori_maisuu = nokori_maisuu.copy()
    temp_aoki_maisuu = aoki_maisuu.copy()
    temp_aoki_maisuu[i] += 1
    temp_nokori_maisuu[i] -= 1
    takahashi_kakuritu = [n / sum(temp_nokori_maisuu) for n in temp_nokori_maisuu]

    aoki_tensuu = 0
    for j in range(1, 10):
        aoki_tensuu += j * 10*temp_aoki_maisuu[j]

    takahashi_tensuu = [0]*10
    for j in range(1, 10):
        if temp_nokori_maisuu[j] == 0:
            continue
        temp_takahashi_maisuu = takahasi_maisuu.copy()
        temp_takahashi_maisuu[j] += 1
        temp_tensuu = 0
        for k in range(1, 10):
            temp_tensuu += k * 10*temp_takahashi_maisuu[k]
        takahashi_tensuu[j] = temp_tensuu

    T = [(t, k) for t, k in zip(takahashi_tensuu, takahashi_kakuritu)]
    for j, (t, k) in enumerate(T):
        if j == 0:
            continue
        if t > aoki_tensuu:
            ans += aoki_kakuritu[i]*takahashi_kakuritu[j]

print(ans)



