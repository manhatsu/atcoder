# from collections import defaultdict, deque
# from itertools import combinations, permutations
# import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

H, W = map(int, input().split())
F = []
for i in range(H):
    F.append(input())

seen = [[0]*W for i in range(H)]
dh = [0, 1, 0, -1]
dw = [1, 0, -1, 0]
identifier = 1
for h in range(H):
    for w in range(W):
        if seen[h][w] or F[h][w] == '.':
            continue
        seen[h][w] = identifier
        Q = deque()
        Q.append((h, w))
        while Q:
            nh, nw = Q.popleft()
            for i in range(4):
                nexh = nh + dh[i]
                nexw = nw + dw[i]
                if nexh < 0 or nexh >= H or nexw < 0 or nexw >=W:
                    continue
                if seen[nexh][nexw] or F[nexh][nexw] == '.':
                    continue
                seen[nexh][nexw] = identifier
                Q.append((nexh, nexw))

        identifier += 1

P = identifier - 1

# for i in range(H):
    # print(*seen[i])

S = 0
num_red = 0
for h in range(H):
    for w in range(W):
        if F[h][w] == '#':
            continue
        num_red += 1
        adj_set = set()
        for i in range(4):
            nexh = h + dh[i]
            nexw = w + dw[i]
            if nexh < 0 or nexh >= H or nexw < 0 or nexw >=W:
                    continue
            if F[nexh][nexw] == '.':
                continue
            adj_set.add(seen[nexh][nexw])        

        S += P - len(adj_set) + 1

ans = pow(num_red, -1, MOD) * S % MOD
print(ans)