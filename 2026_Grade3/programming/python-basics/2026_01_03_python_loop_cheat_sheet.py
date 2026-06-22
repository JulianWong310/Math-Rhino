"""
2026-01-03

1) Why don’t we use an "add" variable for constant growth?
If the value added each time is always the same, we can use the number directly.
We use variables like "add" only when the value changes each step.

2) What is the final value of x?
x represents the current value or position.
If the loop updates x by x = x + add, then the final x is the sum of all add values used each step.

3) What is Sum (S)?
S stores the total of all x values added during the loop.
S = sum of all the x used in the loop

4) How do we calculate add?
add = add + constant
("add" grows every step)

5) How do we calculate x?
x = x + add
(x moves forward by add)

6) How do we calculate sum?
S = S + x
(sum current x into the total)

7) When do we use a for loop?
- When the number of repeats is known
- When looping through a fixed range
e.g. all the numbers from a to b, all the numbers from 1 to n

8) What is important when using a while loop?
- The variable in the condition must be updated; otherwise, it will cause an infinite loop
- Used when we don’t know how many times it will run
- Always check whether the condition should be < n or <= n (off-by-one).

9) When do we need to check off-by-one?
Example:
Stop when x becomes greater than n.
Correct condition:
while x <= n:

10) How to calculate sum of special numbers?
Use a for loop.
In a simple loop like range(1, n+1), i is like x increasing by 1 each step.

11) When do we use count?
Often used in while loops (but can be used in for loops too).
To count how many times something happens
count = count + 1

12) What are initial values?
Initial values affect the result of the loop.
S usually starts at 0
count usually starts at 0
x starts at the given starting position
add starts at the given first step

13) Does order matter?
Yes. Updating variables in a different order can change the result.

Case 1: Update add first, then update x
Example:
On step 1, the step size starts at a.
Before each step, the step size increases by b,
so the first movement uses a + b.
add = add + b
x = x + add

Case 2: Update x first, then update add
Example:
On step 1, the step size starts at a.
After each step, the step size increases by b,
so the first movement uses a, and the second uses a + b.
x = x + add
add = add + b

Therefore, always test the first few steps by hand to check the logic.
"""