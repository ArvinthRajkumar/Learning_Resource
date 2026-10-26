def get_bit(x, i):
    return (x >> i) & 1

def set_bit(x, i):
    return x | (1 << i)

def clear_bit(x, i):
    return x & ~(1 << i)

def toggle_bit(x, i):
    return x ^ (1 << i)

def is_power_of_two(n):
    return n > 0 and n & (n - 1) == 0
