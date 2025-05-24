import heapq

N, K = map(int, input().split())
A = list(map(int, input().split()))
# from icecream import # ic

L = []
for i, a in enumerate(A):
    heapq.heappush(L, (a, i))

def is_ok(j, q, rem): # q: length of queue
    # ic(j, q, rem)
    return j*q <= rem

def bs(ok, ng, q, rem):
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        if is_ok(mid, q, rem):
            ok = mid
        else:
            ng = mid
    return ok

rem = K
temp_eaten_each_box = 0
while True:
    a, i = heapq.heappop(L)
    a -= temp_eaten_each_box
    # ic(a, i)
    if a == 0:
        continue
    r = bs(0, a+1, len(L)+1, rem)
    # ic(0, a+1, len(L)+1, rem)
    # ic(r)
    rem -= r*(len(L)+1)
    # ic(rem)
    temp_eaten_each_box += r
    if r < a:
        heapq.heappush(L, (a-r+temp_eaten_each_box, i))
        break
    if not L:
        break

ans = [0]*N
while L:
    a, i = heapq.heappop(L)
    ans[i] = a - temp_eaten_each_box

i = 0
while rem > 0:
    if ans[i] > 0:
        ans[i] -= 1
        rem -= 1
    i += 1

print(*ans)






