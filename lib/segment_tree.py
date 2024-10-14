# op(x, y): 演算の関数
# 要素（自然数、文字列など）...の集合Sに対して閉じている必要あり。
# 結合法則を満たしている必要あり。op(x , y) = x $ yについて(x $ y) $ z = x $ (y $ z)
# e: 単位元を出力する関数 Sの任意の要素に対して演算しても影響を与えない値

class SegTree:
    def __init__(self, op, e, n, v=None): # op: 演算（関数）, e: 単位元（関数）, n: 要素数, v: 格納する数字列(optional)
        self._n = n
        self._op = op
        self._e = e
        self._log = (n - 1).bit_length()
        self._size = 1 << self._log
        self._d = [self._e()] * (self._size << 1)
        if v is not None:
            for i in range(self._n):
                self._d[self._size + i] = v[i]
            for i in range(self._size - 1, 0, -1):
                self._d[i] = self._op(self._d[i << 1], self._d[i << 1 | 1])
    
    def set(self, p, x):
        p += self._size
        self._d[p] = x
        while p:
            self._d[p >> 1] = self._op(self._d[p], self._d[p ^ 1])
            p >>= 1
    
    def get(self, p):
        return self._d[p + self._size]

    def prod(self, l, r):
        sml, smr = self._e(), self._e()
        l += self._size
        r += self._size
        while l < r:
            if l & 1:
                sml = self._op(sml, self._d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self._op(self._d[r], smr)
            l >>= 1
            r >>= 1
        return self._op(sml, smr)
    
    def all_prod(self):
        return self._d[1]
    
    def max_right(self, l, f):
        assert 0 <= l <= self._n
        assert f(self._e())
        if l == self._n: return self._n
        l += self._size # 葉に移動
        sm = self._e() # 確定した区間の積を保持する変数
        while True:
            while l % 2 == 0: l >>= 1 #　右ノードになるまで
            if not f(self._op(sm, self._d[l])):
                # STEP2
                while l < self._size:
                    l <<= 1
                    if f(self._op(sm, self._d[l])):
                        sm = self._op(sm, self._d[l])
                        l += 1
                return l - self._size
            sm = self._op(sm, self._d[l])
            l += 1
            if l & -l == l: break # f(prod(l, N))=Trueが確定
        return self._n

    def min_left(self, r, f):
        assert 0 <= r <= self._n
        assert f(self._e())
        if r == 0: return 0
        r += self._size
        sm = self._e()
        while True:
            r -= 1
            while r > 1 and r % 2: r >>= 1 # 左子ノードになるまで
            if not f(self._op(self._d[r], sm)):
                # STEP2
                while r < self._size:
                    r = 2 * r + 1 # 右子ノードに移動
                    if f(self._op(self._d[r], sm)):
                        sm = self._op(self._d[r], sm)
                        r -= 1
                return r + 1 - self._size
            sm = self._op(self._d[r], sm)
            if r & -r == r: break
        return 0
