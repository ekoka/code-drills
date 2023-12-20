def reverse_bits(n):
    res = 0
    for _ in range(32):
        res <<= 1  
        res |= n & 1
        n >>= 1
    return res

def reverse_bits(n):
    res = 0
    for _ in range(32):
        res = (res<<1) | (n&1)
        n >>= 1
    return res

def reverse_bits(n):
    res = 0
    for _ in range(32):
        res <<= 1  
        if n & 1:
            res |= 1
        n >>= 1
    return res
