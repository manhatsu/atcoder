
N = int(input())
# N, K = map(int, input().split())
A = list(map(int, input().split()))

twos = [0]*N
threes = [0]*N
rems = [0]*N

for i, a in enumerate(A):
    temp = 0
    while a % 2 == 0:
        a //= 2
        temp += 1
    twos[i] = temp
    temp3 = 0
    while a % 3 == 0:
        a //= 3
        temp3 += 1
    threes[i] = temp3
    rems[i] = a

ret = True
for i in range(1, N):
    if rems[i] != rems[i-1]:
        ret = False
        break

if ret:
    ans = 0
    rem_two = min(twos)
    ans += sum(twos) - rem_two * N
    rem_three = min(threes)
    ans += sum(threes) - rem_three * N

print(ans if ret else -1)








