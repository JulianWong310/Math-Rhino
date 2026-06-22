"""
2026-01-03

Problem 1
Start with:
x = 1
Rules:
While x is less than 50, multiply x by 2
When the loop stops:
Print the final value of x
Print how many times the loop ran
Example Output
64
6
"""
x=1
count=0
while x<50:
    x=x*2
    count=count+1
print(x)
print(count)

"""
Problem 2
Description
A walker starts at position 0.
On step 1, he moves 1 unit.
On step 2, he moves 2 units.
On step 3, he moves 3 units, and so on.
Stop when the position becomes greater than n.
Print how many steps were taken.
Input
One integer n
Output
One integer: number of steps taken
"""
n=int(input())
x=0
add=1
count=0
while x<=n:
    x=x+add
    add=add+1
    count=count+1
print(count)

"""
Problem 3
Look at all numbers from 1 to n.
You are given an integer n
A number is special if:
It is divisible by 3
It is not divisible by 2
Count how many special numbers there are.
Print the answer.
input
20
Example Output
3
"""
n=int(input())
count=0
for i in range(1,n+1):
    if i%3==0 and i%2==1:
        count=count+1
print(count)

"""
Problem 4
Description
Write a function called greet(name).
Rules:
If name is "Alice", return "Hello, Alice!"
Otherwise, return "Hello, friend!"
Start with:
name = "Alice"
Call the function once and print the result.
Example Output
Hello, Alice!
"""
def greet(name):
    if name=="Alice":
        return f"Hello, {name}!"
    else:
        return "Hello, friend!"
print(greet("Alice" ))

