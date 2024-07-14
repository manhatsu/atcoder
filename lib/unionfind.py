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