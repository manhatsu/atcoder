
from math import e


S = input()
T = input()
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))

last_ok = len(T)-1
for i in range(len(T)):
    if S[i] == '?' or T[i] == '?' or S[i] == T[i]:
        continue
    last_ok = i-1
    break

first_ok = 0
for i in range(len(T)):
    if S[-i-1] == '?' or T[-i-1] == '?' or S[-i-1] == T[-i-1]:
        continue
    first_ok = len(T)-i
    break

# print(last_ok, first_ok)

for i in range(len(T)+1):
    if i-1 <= last_ok and i >= first_ok:
        print("Yes")
    else:
        print("No")



