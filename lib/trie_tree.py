# トライ木
# 文字列の長さmとしてO(m)で検索・挿入・削除・辞書順で前後となる文字列の取得ができる

# T = Node() でトライ木のルートノードを作成

class Node:
    def __init__(self):
        self.children = {}
        self.value = None

def find(node, key):
    for c in key:
        if c not in node.children:
            return None
        node = node.children[c]
    return node.value

def insert(node, key, value):
    for c in key:
        if c not in node.children:
            node.children[c] = Node()
        node = node.children[c]
    node.value = value