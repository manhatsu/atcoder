from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from colorama import init
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
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

class UnionFind():
    def __init__(self, w):
        n = len(w)
        self.parent = [-1]*n
        self.rank = [0]*n
        self.siz = [1]*n
        self.weight = w[:]
        self.group_weight = w[:]

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
            rootx, rooty = rooty, rootx
        self.parent[rooty] = rootx
        if self.rank[rootx] == self.rank[rooty]:
            self.rank[rootx] += 1
        self.siz[rootx] += self.siz[rooty]
        self.group_weight[rootx] += self.group_weight[rooty]
        return True
    
    # xを含む根付き木に含まれる頂点数を求める
    def getSize(self, x):
        return self.siz[self.root(x)]
    
    def getGroupWeight(self, x):
        return self.group_weight[self.root(x)]
    
    def addWeight(self, x, delta):
        self.weight[x] += delta
        rootx = self.root(x)
        self.group_weight[rootx] += delta

N = int(input())
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

U = UnionFind([1]*N)

uv = []

for i in range(N-1):
    a, b = map(int, input().split())
    uv.append((a-1, b-1))

init_not_connected = set()
R = int(input())
QQ = []
for _ in range(R):
    query = list(map(int, input().split()))
    QQ.append(query)
    if query[0] == 1:
        x, y = query[1]-1, query[2]
        U.addWeight(x, y)
    else:
        x = query[1]-1
        init_not_connected.add(x)

for i in range(N-1):
    if i in init_not_connected:
        continue
    U.unite(uv[i][0], uv[i][1])

ans = []
QQ = QQ[::-1]
for query in QQ:
    if query[0] == 1:
        x, y = query[1]-1, query[2]
        U.addWeight(x, -y)
    else:
        x = query[1]-1
        g0 = U.getGroupWeight(uv[x][0])
        g1 = U.getGroupWeight(uv[x][1])
        U.unite(uv[x][0], uv[x][1])
        ans.append(abs(g0-g1))
    
ans = ans[::-1]
for a in ans:
    print(a)