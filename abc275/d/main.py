from functools import lru_cache
import math


N = int(input())

@lru_cache(maxsize=None)
def f(n):
    if n == 0:
        return 1
    return f(math.floor(n/2)) + f(math.floor(n/3))

print(f(N))
