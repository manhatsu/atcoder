N = int(input())
# N, K = map(int, input().split())
H = list(map(int, input().split()))

from collections import deque

Q = deque()
ans = 1
ans_list = []
for i in range(N):
    val = 1
    while Q:
        (h, c) = Q.popleft()
        if h <= H[i]:
            val += c
            ans -= h*c
        else:
            Q.appendleft((h, c))
            break
    Q.appendleft((H[i], val))
    ans += H[i]*val
    ans_list.append(ans)

print(*ans_list)








