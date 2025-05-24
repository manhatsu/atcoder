from sortedcontainers import SortedList
# N = int(input())
N, K = map(int, input().split())
S = input()
# A_list = list(map(int, input().split()))

T = [ord(s) - ord('a') for s in S]
I = [[] for _ in range(26)]

for i, t in enumerate(T):
    I[t].append(i)

I = [i[::-1] for i in I]

L = SortedList(T[:len(T)-K+1])

ans = ''

idx_toadd = len(T)-K+1
last_idx = 0
while True:
    # print('L:', L)
    # print('I:', I)
    l = L.pop(0)
    ans += chr(l + ord('a'))
    if len(ans) == K:
        break
    idx = I[l].pop()
    while last_idx < idx:
        t = T[last_idx]
        L.discard(t)
        I[t].pop()
        last_idx += 1
    last_idx = idx + 1
    L.add(T[idx_toadd])
    idx_toadd += 1

print(ans)



