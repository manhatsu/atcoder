N, K = map(int, input().split())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

C = [a-b for a, b in zip(A, B)]

bczip = sorted(zip(B, C))
B, C = zip(*bczip)

invB = [(-1*b, i) for i, b in enumerate(B)]
invC = [(-1*c, -1) for c in C]

# print('invB', invB)
# print('invC', invC)

import heapq

ans = 0
t = 0
heapq.heapify(invB)

while (t < K) and (invB):
    (p, idx) = heapq.heappop(invB)
    # print('pop point={}, idx={}'.format(p, idx))
    ans += p*(-1)
    t += 1

    if idx != -1:
        # print('push point{}'.format(invC[idx][0]))
        heapq.heappush(invB, invC[idx])

print(ans)









