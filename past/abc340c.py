import numpy as np

N = int(input())
n = np.array(N).astype(np.float128)

i = int(np.log2(n))
# print(i)

# print(N * i + 2 * (int(N) - int(2 ** i)))
print(N*(2+i)-2**(i+1))

