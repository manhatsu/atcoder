from collections import deque

##トポロジカルソート
# O(N+M) N頂点数、M辺の数

N = 5 # ノード数
G = [[] for i in range(N)]
into_num = [0]*N # 入次数

def topological_sort(G, into_num):
    #入ってくる有向辺を持たないノードを列挙
    q = deque()

    for i in range(N):
        if into_num[i] == 0:
            q.append(i)
    
    ans = []
    while q:
        v = q.popleft()
        ans.append(v)
        for adj in G[v]:
            into_num[adj] -= 1
            if into_num[adj] == 0:
                q.append(adj) #入次数が0になったら、キューに入れる
    
    return ans

def check(ans, N):
    if len(ans) == N:
        print('閉路なし') #同じ頂点数なら閉路なし
    else:
        print('閉路有り') #頂点数が異なると閉路が存在している
