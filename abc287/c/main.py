N, M = map(int, input().split())
# A_list = list(map(int, input().split()))
import sys
sys.setrecursionlimit(10**7)
from collections import deque

ans = True
if N-1 != M:
    ans = False
if ans:
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)

    for g in G:
        if len(g) > 2:
            ans = False
            break
if ans:
    seen = [0]*N
    seen[0] = 1
    Q = deque()
    Q.append(0)

    while Q:
        v= Q.popleft()
        for lv in G[v]:
            if not seen[lv]:
                seen[lv] = 1
                Q.append(lv)
    
    if any([s == 0 for s in seen]):
        ans = False

print('Yes' if ans else 'No')

'''
class UnionFind():
    # 初期化
    def __init__(self, n):
        self.parent = [-1]*n
        self.rank = [0]*n
        self.siz = [1]*n

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
        return True
    
    # xを含む根付き木に含まれる頂点数を求める
    def getSize(self, x):
        return self.siz[self.root(x)]

ans = True
if M != N-1:
    ans = False
else:
    G = [[] for i in range(N)]
    U = UnionFind(N)
    for _ in range(M):
        u, v = map(int, input().split())
        u, v = u-1, v-1
        if U.isSame(u, v):
            ans = False
            break
        U.unite(u, v)

    # 全てが連結か判定する
    roots = set([U.root(i) for i in range(N)])
    if len(roots) != 1:
        ans = False
'''

# unionfindだと分岐を判定できてない


