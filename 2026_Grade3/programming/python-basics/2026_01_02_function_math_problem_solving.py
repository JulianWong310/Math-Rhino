"""
2026/01/02
 Problem 1
A number sequence starts like this:
2, 4, 7, 11, 16, ?
Each new number is made by adding:
+2, then +3, then +4, then +5, then +6 …
Question:
What is the next number?
"""
add=2
x=2
for i in range(5):
    x=x+add
    add=add+1
print(x)

"""
Problem 2
Write a function called rule(x).
Rules:
If x is even, divide it by 2
If x is odd, add 3
Start with:
x = 7
Repeat the rule until x becomes 1.
Count how many steps it takes.
Print the number of steps.
"""
x=7
count=0
while x>1:
    if x%2==0:
        x=x//2
    else:
        x=x+3
    count=count+1
print(count)

"""
Problem 3
Description
Given two integers a and b (a ≤ b):
From a to b, add all numbers that are:
divisible by 4 or
divisible by 7
Print the final sum.
"""
a= int(input())
b= int(input())
s=0
for i in range(a ,b+1):
    if i % 4 == 0 or i % 7 == 0:
        s=s+i
print(s)

"""
Problem 4
Description
A walker starts at position 0.
On step 1, the walker moves a units
Each step after that, the movement increases by b units
Stop when the position becomes greater than n.
Print how many steps were taken.
Input
a
b
n
"""
a=int(input())
b=int(input())
n=int(input())
x=0
add=a
count=0
while x<n:
    x=x+add
    add=add+b
    count=count+1
print(count)

"""
Problem 5
Write a function called adjust(x).
Rules:
If x is greater than 20, return x - 5
Otherwise, return x + 2
Start with:
x = 18
Call the function once and print the result.
Example Output
20
"""
def adjust(x):
    if x >20:
        return x-5
    else:
        return x+2
print(adjust(18))

"""
Problem 6
Write a function called change(x).
Rules:
If x is less than 10, return x + 3
Otherwise, return x * 2
Start with:
x = 5
Call the function once and print the result.
Example Output
8
"""
def change(x):
    if x<10:
        return x+3
    else:
        return x*2
print(change(5))

"""
Problem 7
Write a function called next_step(x).
Rules:
If x is even, divide it by 2
If x is odd, add 5
Start with:
x = 3
Apply the function 5 times using a loop.
Print the final value of x.
"""
def next_step(x):
    if x % 2==0:
        return x/2
    else:
        return x+5
x=3
for i in range (5) :
    x=next_step(x) # 8, 4, 2, 1, 6
print(x)