"""
2026/03/04
The Water Jug Challenge
You have two jugs with capacities:
A liters
B liters
You may add or pour water in full jug amounts.
Determine whether it is possible to measure exactly K liters.
Input
A
B
K
Output
Yes
or
No
🪣🐍
"""
A=int(input())
B=int(input())
K=int(input())
import math
d=math.gcd(A,B)
if K%d==0:
    print("Yes")
else:
    print("No")


