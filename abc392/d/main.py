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

N = int(input())
# N, K = map(int, input().split())
K = []

Q = []

for i in range(N):
    L = list(map(int, input().split()))
    K.append(L[0])
    A = L[1:]
    A = sorted(A)
    num = 1
    dig = A[0]
    q = []
    if len(A) == 1:
        q.append((dig, num))
        Q.append(q)
        continue
    for i in range(1, len(A)):
        if A[i] != A[i-1]:
            q.append((dig, num))
            num = 1
            dig = A[i]
        else:
            num += 1
    q.append((dig, num))
    Q.append(q)

ans = 0
for i in range(N):
    for j in range(i+1, N):
        Q1 = deque(Q[i])
        Q2 = deque(Q[j])
        dig1, num1 = Q1.popleft()
        dig2, num2 = Q2.popleft()
        temp = 0.0
        while True:
            if dig1 == dig2:
                temp += num1 / K[i] * num2 / K[j]
                if Q1 and Q2:
                    dig1, num1 = Q1.popleft()
                    dig2, num2 = Q2.popleft()
                else:
                    break
            elif dig1 < dig2:
                if Q1:
                    dig1, num1 = Q1.popleft()
                else:
                    break
            else:
                if Q2:
                    dig2, num2 = Q2.popleft()
                else:
                    break
        ans = max(ans, temp)

print(ans)
                
            
