"""
2026/02/22
The Rules Refresher
1.  **Rule 1 (Transitivity):** If $a|b$ and $b|c$, then $a|c$.
2.  **Rule 2 (Add/Sub):** If $m|a$ and $m|b$, then $m|(a+b)$ and $m|(a-b)$.
3.  **Rule 3 (Combo):** If $m|a$ and $m|b$, then $m|(qa + rb)$ for any integers $q, r$.
"""

"""
Problem 1 — Transitive Divisibility
An integer a divides an integer b if b % a == 0.
You are given three positive integers a, b, and c.
It is known that:
a divides b
b divides c
Task
Determine whether a must divide c.
Print True if a divides c.
Otherwise, print False.
Input
Three integers:
a
b
c
Output
True
or
False
Example
Input
3
12
36
Output
True
"""
a=int(input())
b=int(input())
c=int(input())
print(c%a==0)

"""
Problem 2 — Add and Subtract Rule
You are given three integers m, a, and b.
It is known that:
m divides a
m divides b
Task
Check whether:
m divides (a + b)
m divides (a - b)
Print two lines:
True or False for (a + b)
True or False for (a - b)
Input
m
a
b
Example
Input
5
20
35
Output
True
True
"""
m=int(input())
a=int(input())
b=int(input())
print((a+b)%m==0)
print((a-b)%m==0)

"""
Problem 3 — Linear Combination Rule
You are given five integers:
m
a
b
q
r
It is known that:
m divides a
m divides b
Define a new number:
X = q * a + r * b
Task
Determine whether m divides X.
Print True or False.
Example
Input
4
12
20
3
-2
Output
True
Explanation:
Since:
4 divides 12
4 divides 20
Then 4 must divide any linear combination of them.
"""
m=int(input())
a=int(input())
b=int(input())
q=int(input())
r=int(input())
print((q*a+r*b)%m==0)

"""
Problem 5 — Conditional Divisibility Challenge
You are given six integers:
m
a
b
c
q
r
Unlike simpler problems, it is NOT guaranteed that:
m divides a
m divides b
a divides c
You must first verify whether the required divisibility conditions are satisfied.
Task
Follow these steps carefully:
If m does not divide a OR m does not divide b,
print:
Invalid Input
and stop the program.
Otherwise, determine whether the following are true:
Does m divide c?
Does m divide (a + b)?
Does m divide (q·a + r·b)?
Print three lines:
True or False
True or False
True or False
📥🐍 Input
Six integers, one per line.
🧾 Example 1 (Valid Case)
Input
4
12
20
36
3
-2
Output
True
True
True
🧾🎯 Example 2 (Invalid Case)
Input
5
12
20
30
1
1
Output
Invalid Input
Because 5 does NOT divide 12.
"""
m=int(input())
a=int(input())
b=int(input())
c=int(input())
q=int(input())
r=int(input())
if a%m==0 and b%m==0:
    print(c%m==0)
    print((a+b)%m==0)
    print((q*a+r*b)%m==0)
else:
    print("Invalid Input")
