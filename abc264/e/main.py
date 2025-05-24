from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
# from icecream import # ic
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, M, E = map(int, input().split())
# A = list(map(int, input().split()))
# ic(N, M, E)

F = []
for _ in range(E):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    F.append((u, v))

H = []
Q = int(input())
S = set()
for _ in range(Q):
    x = int(input())
    x -= 1
    H.append(F[x])
    S.add(x)

H = H[::-1]

# ic(H)

class UnionFind():
    # 初期化
    def __init__(self, n, m):
        self.parent = [-1]*(n+m)
        self.rank = [0]*(n+m)
        self.siz = [1]*(n+m)
        self.hasdenki = [0]*(n+m)
        for i in range(n, n+m):
            self.hasdenki[i] = 1
        self.num_hasdenki = m

    # rootを求める
    def root(self, x):
        if self.parent[x] == -1:
            return x
        self.parent[x] = self.root(self.parent[x])
        return self.parent[x]
    
    # xとyのrootが一致するか判定
    def isSame(self, x, y):
        return self.root(x) == self.root(y)
    
    # xを含むグループとyを含むグループを併合
    def unite(self, x, y):
        # ic(x, y)
        # ic(self.hasdenki)
        # ic(self.num_hasdenki)
        rootx = self.root(x)
        rooty = self.root(y)
        if rootx == rooty:
            return False
        if self.rank[rootx] < self.rank[rooty]:
            rootx, rooty = rooty, rootx # rooty側のrankを小さくしておく
        self.parent[rooty] = rootx # rootyをrootxの子とする
        if self.rank[rootx] == self.rank[rooty]:
            self.rank[rootx] += 1
        # ic(self.hasdenki[rootx], self.hasdenki[rooty])
        if self.hasdenki[rootx] and (not self.hasdenki[rooty]):
            self.num_hasdenki += self.siz[rooty]
        elif (not self.hasdenki[rootx]) and self.hasdenki[rooty]:
            self.num_hasdenki += self.siz[rootx]
        self.hasdenki[rootx] |= self.hasdenki[rooty]
        # ic(self.hasdenki)
        # ic(self.num_hasdenki)
        self.siz[rootx] += self.siz[rooty]
        return True
    
    # xを含む根付き木に含まれる頂点数を求める
    def getSize(self, x):
        return self.siz[self.root(x)]
    
    def getNumHasDenki(self):
        # ic(self.hasdenki)
        return self.num_hasdenki

ans = []
U = UnionFind(N, M)
for i, (u, v) in enumerate(F):
    if i in S:
        continue
    U.unite(u, v)

ans.append(U.getNumHasDenki()-M)

for u, v in H:
    U.unite(u, v)
    ans.append(U.getNumHasDenki()-M)

ans = ans[::-1]

for a in ans[1:]:
    print(a)
