"""
The Mysterious Steps

Julian starts at 0. He can jump forward by A or B.
Determine if he can land EXACTLY on step X.

Output:
0 if it is possible.
-1 if it is impossible.
"""
A=int(input())
B=int(input())
K=int(input())
import math
d=math.gcd(A,B)
if K % d== 0:
    print(0)
else:
    print(-1)
