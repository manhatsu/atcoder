import math

K = int(input())

def combi(n, m):
    return math.factorial(n) // (math.factorial(n-k) * math.factorial(k))

# 何桁か見積もる
ndigits = 1
temp = -1
for i in range(1, 11):
    temp += combi(n, i)
    if temp >= K:
        break
    ndigits += 1

for i in range(1, )



