from math import gcd

def gcd_of_strings(s, t):
    if s + t != t + s:
        return ""
    return s[:gcd(len(s), len(t))]
