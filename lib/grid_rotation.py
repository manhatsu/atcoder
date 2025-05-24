

def right_rot90(S): # 時計回り90度
  return list(zip(*S[::-1]))

def left_rot90(S):
    return list(zip(*S))[::-1]   