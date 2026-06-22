# Find gcd (50,20)

# Method 1
# Subtraction-based Euclidean Algorithm
# Find gcd(a, b) using repeated subtraction

a = 50
b = 20

# Loop until both numbers are equal
while a != b:
    if a > b:
        a -= b # r1: a=30, r2: a=10
    else:
        b -= a  # r3: b= 10
# Print the result
print("GCD:", a)

# Method 2
# Euclidean Algorithm using Modulo (%)
a = 50
b = 20

# Loop until b = 0
while b != 0:
    # The Logic: GCD(a, b) is the same as GCD(b, a % b)
    a, b = b, a % b # r1: a,b=20,10   r2: a,b=10,0

print("GCD:", a)