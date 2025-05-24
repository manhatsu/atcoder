
from cProfile import label


N = int(input())
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))
L = []
for i in range(N):
    a, c = map(int, input().split())
    L.append((a, c, i+1))

L = sorted(L)[::-1]
# print(L)

prev_c = 0
prev_a = 0
suteru_list = []
for a, c, j in L:
    if prev_a > a and prev_c < c:
        suteru_list.append(j)
    else:
        prev_c = c
        prev_a = a

suteru_set = set(suteru_list)
        
        
nokosu_list = [i+1 for i in range(N) if i+1 not in suteru_set]

print(len(nokosu_list))
if len(nokosu_list) > 0:
    print(*nokosu_list)





