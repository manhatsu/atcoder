from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
sys.set_int_max_str_digits(10000000)
sys.setrecursionlimit(4100000)
import heapq
try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

import typing


class DSU:

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.parent_or_size = [-1] * n

    def add(self) -> int:
        self.parent_or_size.append(-1)
        self._n += 1
        return self._n - 1

    def merge(self, a: int, b: int) -> int:
        assert 0 <= a < self._n
        assert 0 <= b < self._n

        x = self.leader(a)
        y = self.leader(b)

        if x == y:
            return x

        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y = y, x

        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x

        return x

    def same(self, a: int, b: int) -> bool:
        assert 0 <= a < self._n
        assert 0 <= b < self._n

        return self.leader(a) == self.leader(b)

    def leader(self, a: int) -> int:
        assert 0 <= a < self._n
        if self.parent_or_size[a] < 0:
            return a
        self.parent_or_size[a] = self.leader(self.parent_or_size[a])
        return self.parent_or_size[a]

    def size(self, a: int) -> int:
        assert 0 <= a < self._n

        return -self.parent_or_size[self.leader(a)]

    def groups(self) -> typing.List[typing.List[int]]:
        leader_buf = [self.leader(i) for i in range(self._n)]

        result: typing.List[typing.List[int]] = [[] for _ in range(self._n)]
        for i in range(self._n):
            result[leader_buf[i]].append(i)

        return list(filter(lambda r: r, result))

N, Q = map(int, input().split())

P = []

def rotate45(x, y):
    return x+y, x-y

for i in range(N):
    x, y = map(int, input().split())
    P.append(rotate45(x, y))

U = DSU(N)

for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x, y = query[1], query[2]
        U.add()
        P.append(rotate45(x, y))
    
    elif query[0] == 2:
        root_dict = defaultdict(list)
        for j in range(len(P)):
            root_dict[U.leader(j)].append(j)

        roots = list(root_dict.keys())
        if len(roots) < 2:
            print(-1)
            continue

        min_dist = INF
        edges = []
        for i in range(len(P)): 
            for j in range(i + 1, len(P)):
                if U.same(i, j):
                    continue
                d = max(abs(P[i][0] - P[j][0]), abs(P[i][1] - P[j][1]))
                if d < min_dist:
                    min_dist = d
                    edges = [(i, j)]
                elif d == min_dist:
                    edges.append((i, j))

        for u, v in edges:
            d = max(abs(P[u][0] - P[v][0]), abs(P[u][1] - P[v][1]))
            if d == min_dist:
                U.merge(u, v)

        print(min_dist)

    elif query[0] == 3:
        u, v = query[1], query[2]
        u, v = u-1, v-1
        print('Yes' if U.same(u, v) else 'No')