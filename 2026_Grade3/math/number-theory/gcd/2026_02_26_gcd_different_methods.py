"""
2026/02/26
Euclidean Algorithm Comparison

+----------------------+----------------------+
| Subtraction Model    | Modulo Model         |
+----------------------+----------------------+
| Repeated a -= b      | Single A % B         |
| Slower               | Faster               |
| Same math principle  | Same math principle  |
| O(max(a, b))         | O(log n)             |
+----------------------+----------------------+

Explanation:

Subtraction Model:
- Subtracts the smaller number from the larger one many times.
- If numbers are very different, it may take many steps.

Modulo Model:
- Uses remainder (%) to reduce the numbers quickly.
- Each step makes the numbers much smaller.

Conclusion:
Both methods are mathematically correct,
but the modulo version is much more efficient
and is preferred in programming contests.
"""
# Find GCD ( -1859, 1573)
# Method 1
num1, num2 = -1859, 1573
a=abs(num1)
b=abs(num2)
while b!=0:
    a,b=b,a%b
print(a)
print("🐍")
# What if a < b?? what will happen?
# Add one more step at the beginning to switch the positions of a,b

#Method 2
import math
print(math.gcd(-1859,1573))

"""
Problem  — Greatest Common Divisor
Given two positive integers A and B, determine their greatest common divisor (GCD).
The greatest common divisor of two integers is the largest positive integer that divides both numbers.
Input
Two positive integers:
A
B
Output
Print a single integer representing:
gcd(A, B)
Example 1
Input
12
18
Output
6
Example 2
Input
35
49
Output
7
"""
# Method 1
a=int(input())
b=int(input())
while b!=0:
    a,b=b,a%b
print(a)
print("🐍")

# Method 2
a=int(input())
b=int(input())
import math
print(math.gcd(a,b))
print("🐍")

