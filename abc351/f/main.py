from bisect import bisect_left, bisect_right
from atcoder import fenwicktree
from atcoder.lazysegtree import LazySegTree

N = int(input())
# N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
L = sorted(A)

V = [0]*N

def op(x, y):
    return x + y

e = 0

def mapping(f, x):
    return f + x

def composition(f, g):
    return f + g

id = 0

F0 = LazySegTree(op, e, mapping, composition, id, V)
F1 = LazySegTree(op, e, mapping, composition, id, V)

# F0 = fenwicktree.FenwickTree(N)
# F1 = fenwicktree.FenwickTree(N)

for i in reversed(range(N)):
    idx = bisect_left(L, A[i])

    # c = F0.sum(idx, N)
    # s = F1.sum(idx, N)
    c = F0.prod(idx, N)
    s = F1.prod(idx, N)

    # F0.add(idx, 1)
    # F1.add(idx, A[i])
    F0.set(idx, F0.get(idx) + 1)
    F1.set(idx, F1.get(idx) + A[i])

    ans += s - c * A[i]

print(ans)