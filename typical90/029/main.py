from atcoder.lazysegtree import LazySegTree

W, N = map(int, input().split())

L = [0]*W

INF = 1<<63
ID = INF

def op(ele1, ele2):
    return max(ele1, ele2)

def mapping(f, x):
    if f == ID:
        return x
    return f

def composition(f, g):
    if f == ID:
        return g
    return f

e = -INF
id_ = ID

T = LazySegTree(op, e, mapping, composition, id_, L)

for _ in range(N):
    l, r = map(int, input().split())
    l -= 1
    x = T.prod(l, r)
    print(x+1)
    T.apply(l, r, x+1)