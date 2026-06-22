def gcd(a, b):
    while b!=0:
        a, b = b, a % b
    return a

def lcm(a, b):
    # Apply the Magical Formula
    return (a * b) // gcd(a, b)

# Test
print(lcm(12, 18))  # Output: 36