from collections import defaultdict, deque
from hmac import new
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

N, M = map(int, input().split())
# A = list(map(int, input().split()))

A = []
rem_underbars = 16
for i in range(N):
    a = input()
    A.append(a)
    rem_underbars -= len(a)
rem_underbars -= N-1

class Node:
    def __init__(self):
        self.children = {}
        self.value = None

def find(node, key):
    for c in key:
        if c not in node.children:
            return False # None
        node = node.children[c]
    return node.value == 1

def insert(node, key, value):
    for c in key:
        if c not in node.children:
            node.children[c] = Node()
        node = node.children[c]
    node.value = value

root = Node()
if M > 0:
    for _ in range(M):
        T = input()
        insert(root, T, 1)

if N == 1:
    if len(A[0]) < 3:
        print(-1)
    elif find(root, A[0]):
        print(-1)
    else:
        print(A[0])
    exit()

def dfs(U, cur, rem_underbars):
    # ic(U, cur, rem_underbars)
    V = U + B[cur]
    cur += 1
    if cur == N:
        if find(root, V):
            return False
        else:
            return V
    for r in range(0, rem_underbars+1):
        ret = dfs(V + '_' + '_'*r, cur, rem_underbars-r)
        if ret:
            return ret

    return False

L = list(permutations(A))

# ic(rem_underbars)

for B in L:
    X = dfs('', 0, rem_underbars)
    if X:
        print(X)
        exit()

print(-1)