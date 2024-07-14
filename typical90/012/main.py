H, W = map(int, input().split())
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))

Q = int(input())

class UnionFind():
    def __init__(self, n):
        self.parent = [-1]*n
        self.rank = [0]*n
        self.siz = [0]*n

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
        self.siz[rootx] = self.siz[rooty]
        return True
    
    def getSize(self, x):
        return self.siz[self.root(x)]

# indexはi*W+jで管理する
def to1d(i, j, W):
    return i*W+j  

def to2d(idx_1d, W):
    i = idx_1d // W
    j = idx_1d % W

U = UnionFind(H*W)
F = [[0]*W for _ in range(H)]

dh = [0, 1, 0, -1]
dw = [1, 0, -1, 0]

for _ in range(Q):
    q_list = list(map(int, input().split()))
    if q_list[0] == 1:
        nowh, noww = [q-1 for q in q_list[1:]]
        # print(nowh, noww)
        if F[nowh][noww] == 1:
            continue
        F[nowh][noww] = 1
        for i in range(4):
            sh = nowh + dh[i]
            sw = noww + dw[i]
            if (0 <= sh < H) and (0 <= sw < W):
                if F[sh][sw] == 1:
                    # print('Unite {}, {} with {}, {}'.format(nowh,noww, sh, sw))
                    U.unite(to1d(nowh, noww, W), to1d(sh, sw, W))

    else:
        ra, ca, rb, cb = [q-1 for q in q_list[1:]]

        if (F[ra][ca] == 1) and (F[rb][cb] == 1):
            # print(to1d(ra, ca, H))
            # print(to1d(rb, cb, H))
            ret = U.isSame(to1d(ra, ca, W), to1d(rb, cb, W))
            print('Yes' if ret else 'No')
        else:
            print('No')