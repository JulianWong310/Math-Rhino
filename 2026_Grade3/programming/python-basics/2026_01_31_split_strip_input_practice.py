"""
2026/01/31

| Input Pattern          | Correct Input Handling                                              | Notes / Output                                                                                       |
| ---------------------- | ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `ADD`                  | `word = input().strip()`                                            | Single word or command; removes leading/trailing spaces; use directly as string                      |
| `A B A B A`            | `commands = input().split()`                                        | Multiple elements in one line, space-separated → list `['A','B','A','B','A']`                        |
| `1 2 3 4`              | `nums = list(map(int, input().split()))`                            | Multiple numbers in one line, space-separated → integer list `[1,2,3,4]`                             |
| `RRUULDR`              | `s = input().strip(); for c in s:` or `lst = list(input().strip())` | Continuous characters, no spaces → iterate each character or convert to list for indexing            |
"""

""" 
Part 1 — Single Word (strip)
Problem 1
Description:
Read a single command and print it.
Input Example:
ADD
Solution:
Output:
ADD
"""
cmd = input().strip()
print(cmd)

"""
Problem 2 
You are given one command on a single line.
The command may contain extra spaces at the beginning or end.
If the command is "fish", print yes.
Otherwise, print no.
"""
cmd = input().strip()
if cmd == "fish":
    print("yes")
else:
    print("no")

"""
Part 2 — Multiple Elements in One Line (split)
Problem 1
Read a line of commands separated by spaces and print them as a list.
Input Example:
A B A B A
Output:
['A', 'B', 'A', 'B', 'A']
"""
cmd=input().split()
print(cmd)

"""
Problem 2 
Problem Description
You are given a sequence of commands separated by spaces.
Each command is either A or B.
Count how many times the command A appears.
Input
A B A B A
"""
cmd=input().split()
count=0
for x in cmd:
    if x == "A":
        count+=1
print(count)

"""
Part 3  — Numbers in One Line (map + split)
Problem 3
Read a line of numbers separated by spaces and print the largest number.
Input Example:
1 2 3 4
Output:
4
"""
nums=list(map(int,input().split()))
largest=float("-inf")
for x in nums:
    if largest < x:
        largest=x
print(largest)

"""
Part 4 — Continuous Characters (no spaces)
Problem 1 
Description:
Read a string of continuous characters and print each character on a separate line.
Input Example:
RRUULDR
Output:
R
R
U
U
L
D
R
"""
# Method 1: use string directly
cmd=input().strip()
for x in cmd:
    print(x)

# Method 2: use list
cmd=list(input().strip())
print(cmd)
for x in cmd:
    print(x)

"""
Problem 2
Problem Description
You are given a string of movement commands with no spaces.
Each character represents a direction:
R → right
L → left
U → up
D → down
Starting from (0, 0), print the final position.
Input
RRUULDR
"""
x,y=0,0
s=input().strip()
for e in s:
    if e=="R":
        x=x+1
    elif e=="L":
        x=x-1
    elif e=="U":
        y=y+1
    elif e=="D":
        y=y-1
print(x,y)

