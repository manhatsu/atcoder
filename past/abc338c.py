import numpy as np

N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

qa = [q // a if a > 0 else np.inf for q, a in zip(Q, A)]
maxa = min(qa)

ret = 0
for alpha in range(0, maxa+1):
    ba = [(q-a*alpha) // b if b > 0 else np.inf for q, a, b in zip(Q, A, B)]
    beta = min(ba)
    if alpha + beta > ret:
        ret = alpha + beta

print(ret)