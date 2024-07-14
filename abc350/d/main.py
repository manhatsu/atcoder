class UnionFind():
    def __init__(self, n):
        self.parent = [-1]*n
        self.rank = [0]*n
        self.siz = [1]*n

    def root(self, x):
        if self.parent[x] == -1:
            return x
        self.parent[x] = self.root(self.parent[x])
        return self.parent[x]
    
    def isSame(self, x, y):
        return self.root(x) == self.root(y)
    
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
        return True
    
    def getSize(self, x):
        return self.siz[self.root(x)]

import math 
def NCM(N, M):
    return math.factorial(N) / (math.factorial(N-M) * math.factorial(M))

N, M = map(int, input().split())
# A_list = list(map(int, input().split()))

F = UnionFind(N)
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    F.unite(a, b)

root_set = set()
for i in range(N):
    # if not F.root(i) in root_set:
    root_set.add(F.root(i))

# print(root_set)

ans = 0
for r in root_set:
    p = F.getSize(r)
    if p == 1:
        continue
    ans += NCM(p, 2)

ans -= M
print(int(ans))


    



