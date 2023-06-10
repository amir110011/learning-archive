def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

print gcd(1,21)
