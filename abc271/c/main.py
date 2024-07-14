from collections import defaultdict, deque
from sortedcontainers import SortedSet
N = int(input())
A = list(map(int, input().split()))

rem = 0 # 交換に使える冊数
K = set()
for a in A:
    if not a in K:
        K.add(a)
    else:
        rem += 1

K = SortedSet(K)
# print('rem', rem)
       
Q = deque(K)
# print(Q)


now = 1 # 現在読みたい巻数
endloop = False
while Q:
    x = Q[0]
    # print('x', x)
    while x > now:
        # print('x, now', x, now)
        while rem < 2: # 交換冊数が足りないときは巻番号の大きい方から取る
            if not Q:
                endloop = True
                break
            y = Q.pop()
            rem += 1
        if endloop:
            break
        now += 1
        rem -= 2
    if endloop:
        break
    if not Q:
        break
    _ = Q.popleft()
    now += 1

# 余った冊数を変換
while rem >= 2:
    rem -= 2
    now += 1

print(now-1)
        
        








