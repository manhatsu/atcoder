import math
# import numpy as np

D = int(input())
# D = np.array(D).astype(np.float128)

maxx = int(math.sqrt(D))

# X2 = [x ** 2 for x in range(0, maxx+1)]


ret = int((maxx+1)**2-D)
x = 1
y = maxx
while x <= y:
    if D > x**2:
        ylow = int(math.sqrt(D-x**2))
    else:
        ylow = 0
    temp = int(-(x**2+ylow**2-D))
    if ret > temp:
        ret = temp
    yhigh = ylow+1
    temp = int(x**2+yhigh**2-D)
    if ret > temp:
        ret = temp
    x += 1

print(ret)