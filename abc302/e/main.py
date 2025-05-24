
N, Q = map(int, input().split())
# A_list = list(map(int, input().split()))

idp_node_num = N

G = [set() for i in range(N)]

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        u, v = q[1]-1, q[2]-1
        if len(G[u]) == 0:
            idp_node_num -= 1
        if len(G[v]) == 0:
            idp_node_num -= 1
        G[u].add(v)
        G[v].add(u)
    else:
        v = q[1]-1
        if len(G[v]) > 0:
            for lv in G[v]:
                G[lv].discard(v)
                if len(G[lv]) == 0:
                    idp_node_num += 1
            G[v] = set()
            idp_node_num += 1
    print(idp_node_num)



