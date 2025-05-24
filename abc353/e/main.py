from collections import deque
import math

N = int(input())
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))

S = list(input().split())
S = sorted(S)

init = [-1]*26

D = [[0, []] for _ in range(300001)]
D[0][1] = init.copy()

ans = 0
key2set = 1
for T in S:
    nowkey = 0
    for s in T:
        b = ord(s) - ord('a')
        if D[nowkey][1][b] == -1:
            D[nowkey][1][b] = key2set
            D[key2set][1] = init.copy()
            nowkey = key2set
            key2set += 1
            continue
        else:
            nowkey = D[nowkey][1][b]
            D[nowkey][0] += 1
            ans += D[nowkey][0]

print(ans)

        



