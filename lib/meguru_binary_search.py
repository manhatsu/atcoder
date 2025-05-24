def is_ok(idx):
    return # idxに対する判定条件

def bs(ok, ng): # okの初期値は-1, ngの初期値は最大idx+1
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

# 三分探索
# pythonは小数の桁落ちが起こる。epsを小さくしすぎると無限ループに陥る

def ternary_search(l, r, func, is_max=True, eps=1e-4):
    # is_max: 最大値を求める場合は True, 最小値は False
  
    while r - l > eps:
        m1 = l + (r - l) / 3
        m2 = r - (r - l) / 3
        f1, f2 = func(m1), func(m2)
        
        if (is_max and f1 < f2) or (not is_max and f1 > f2):
            l = m1  # 右側に極値がある
        else:
            r = m2  # 左側に極値がある
    
    return (l + r) / 2  # 極値を持つ x の近似値

# example usage
f = lambda x: -(x-2)**2 + 4 # 関数
x_opt = ternary_search(-10, 10, f, is_max=True)
print(x_opt, f(x_opt))


