T = int(input())
L, X, Y = map(int, input().split())
# A_list = list(map(int, input().split()))

import numpy as np
import math

def getAngle(e):
    theta = np.radians(360*e/T)
    # print('theta', theta)
    # print('now Takahashi at', 0, -L/2*np.sin(theta), -L/2*np.cos(theta)+L/2)
    mot = math.sqrt(X**2 + (Y + L/2*np.sin(theta))**2)
    chi = -L/2*np.cos(theta)+L/2
    return np.degrees(np.arctan(chi/mot))

Q = int(input())
for _ in range(Q):
    e = int(input())
    print(getAngle(e))




