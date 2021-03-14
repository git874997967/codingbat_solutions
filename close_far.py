def close_far(a, b, c):
    if abs(a - b )  <= 1:
        if  abs(c - b) >= 2 and abs(c - a) >= 2:
            return True
    elif abs(a - c) <= 1:
        if abs(b - a) >= 2 and abs(b - c) >= 2:
            return True  

    return False  