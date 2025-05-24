from collections import defaultdict, deque
from itertools import combinations, permutations
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedDict, SortedList
import math
import sys
sys.setrecursionlimit(4100000)
# def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

# トライ木
# 文字列の長さmとしてO(m)で検索・挿入・削除・辞書順で前後となる文字列の取得ができる

class Node:
    def __init__(self):
        self.children = {}
        self.value = None
        self.count_y = 0 # Yとして追加された個数
        self.is_x = False # Xとして追加されたかどうか

def find(node, key):
    for c in key:
        if c not in node.children:
            return None
        node = node.children[c]
    return node.value

def insert_x(node, key):
    tree = node
    for c in key:
        if c not in node.children:
            node.children[c] = Node()
        node = node.children[c]
        if node.is_x:
            return 0
    node.is_x = True
    ret = node.count_y
    add_count(tree, key, -ret)
    return -ret

def insert_y(node, key):
    tree = node
    for c in key:
        if c not in node.children:
            node.children[c] = Node()
        node = node.children[c]
        if node.is_x:
            return 0
    add_count(tree, key, 1)
    return 1

def add_count(node, key, count):
    for c in key:
        node = node.children[c]
        node.count_y += count

Q = int(input())

T = Node()

ans = 0
for _ in range(Q):
    query = input().split()
    if int(query[0]) == 1:
        key = query[1]
        ans += insert_x(T, key)
    elif int(query[0]) == 2:
        key = query[1]
        ans += insert_y(T, key)
    print(ans)