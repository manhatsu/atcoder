N = int(input())
A, B, C = sorted(list(map(int, input().split())))
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))

# maxC = min(9999, N // C) # C円硬貨の最大枚数

'''
ret = 10000
for i in range(10000):
    for j in range(10000):
        temp = A*i+B*j
        if (temp <= N) and ((N-temp) % C == 0):
            cand = i + j + (N-temp) // C
            if ret > cand:
                ret = cand
print(ret)
'''
        
maxC = N // C

ret = 10000
for i in range(maxC+1):
    price = N - C*i
    maxB = price // B
    for j in range(maxB+1):
        nokori = price - B*j
        if nokori % A == 0:
            maisuu = i + j + nokori // A
            if maisuu < ret:
                ret = maisuu

print(ret)

# ojtだと8 sと出るが，pypyで提出すると100 ms程度（PCインストール済みのpythonが遅い？？）






