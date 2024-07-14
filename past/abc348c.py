import numpy as np
N = int(input())
A = []
C = []

for _ in range(N):
    a, c = map(int, input().split())
    A.append(a)
    C.append(c)

S = sorted(C)
ranking = {x:i+1 for i, x in enumerate(S)}
C_zaatsu = []

for c in C:
    C_zaatsu.append(ranking[c])

min_list = [0]*(len(C_zaatsu)+1)

for i, a in enumerate(A):
    if (min_list[C_zaatsu[i]] == 0) or (min_list[C_zaatsu[i]] > a):
        min_list[C_zaatsu[i]] = a

print(max(min_list))
    

