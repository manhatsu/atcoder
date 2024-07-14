from collections import deque
N = int(input())
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))
dic = {}
for i in range(N):
    a, b = map(int, input().split())
    if a not in dic.keys():
        dic[a] = {b}
    else:
        dic[a].add(b)
    if b not in dic.keys():
        dic[b] = {a}
    else:
        dic[b].add(a)

# 1からつながるグラフが無い場合1を返す
if 1 not in dic.keys():
    maxB = 1
else:
    zaatsu = {} # 登場する階数の座圧
    for i, k in enumerate(dic.keys()):
        zaatsu[k] = i

    # print(zaatsu)

    # BFS
    maxB = 1 # 最大到達階
    seen = [0]*len(dic)
    seen[zaatsu[1]] = 0
    Q = deque([1])
    while Q:
        v = Q.popleft()
        for lv in dic[v]:
            if seen[zaatsu[lv]] != 0:
                continue
            seen[zaatsu[lv]] = 1
            if lv > maxB:
                maxB = lv
            Q.append(lv)

print(maxB)

