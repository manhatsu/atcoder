# from collections import defaultdict, deque
# from itertools import combinations, permutations
# import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
from sortedcontainers import SortedList
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, Q = map(int, input().split())

class UnionFind():
    # 初期化
    def __init__(self, n):
        self.parent = [-1]*n
        self.rank = [0]*n
        self.siz = [1]*n
        self.sets = [SortedList([i]) for i in range(n)]

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
        rootx = self.root(x)
        rooty = self.root(y)
        if rootx == rooty:
            return False
        if self.rank[rootx] < self.rank[rooty]:
            rootx, rooty = rooty, rootx # rooty側のrankを小さくしておく
        self.parent[rooty] = rootx # rootyをrootxの子とする
        if self.rank[rootx] == self.rank[rooty]:
            self.rank[rootx] += 1
        self.siz[rootx] += self.siz[rooty]
        self.sets[rootx].update(self.sets[rooty])
        self.sets[rooty].clear()
        return True
    
    # xを含む根付き木に含まれる頂点数を求める
    def getSize(self, x):
        return self.siz[self.root(x)]
    
    def getKthLargest(self, x, k):
        r = self.root(x)
        if k > len(self.sets[r])-1:
            return -2
        return self.sets[r][-k-1]
    
U = UnionFind(N)
    
for i in range(Q):
    q, u, v = map(int, input().split())
    u = u-1
    v = v-1
    if q == 1:
        U.unite(u, v)
    else:
        ret = U.getKthLargest(u, v)
        print(ret+1)
