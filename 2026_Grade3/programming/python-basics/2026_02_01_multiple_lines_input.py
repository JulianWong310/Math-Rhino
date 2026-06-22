"""
2026/02/01

Input Pattern                    | Correct Input Handling                              | Notes / Output
-------------------------------- | --------------------------------------------------- | ----------------------------------------------
Multiple lines (words)           | for _ in range(N):                                  | Directly process each word as you read it,
                                 |     word = input().strip()                          | no list needed

Multiple lines (words)           | words = [input().strip()                            | Store all words in a list for later use
                                 |          for _ in range(N)]                         | (indexing, sorting, searching)

Multiple lines (numbers)         | for _ in range(N):                                  | Directly process each number as you read it,
                                 |     num = int(input())                              | no list needed

Multiple lines (numbers)         | nums = [int(input())                                | Store all numbers in a list for later use
                                 |         for _ in range(N)]                          | (math, sorting, comparisons)

Unknown count (numbers)          | while True:                                         | Number of inputs is NOT given.
(stop by condition / break)      |     num = int(input())                              | Stop when a condition is met (break).
                                 |     if <condition>:                                 | Very common in CCC simulations.
                                 |         break

"""

"""
Part 5.1 — Multiple Lines (words)
Problem 1
Description:
Read N words, one per line, and store them in a list. Then print the list.
Input Example:
5
cat
dog
bird
fish
cow
Output:
['cat', 'dog', 'bird', 'fish', 'cow']
"""
# Method 1
N = int(input())
lst=[]
for _ in range(N):
    lst.append(input().strip())
print(lst)

# Method 2
N= int(input())
lst=[input().strip() for _ in range(N)]
print(lst)

"""
Problem 2 — Multiple Lines (strip)
Problem Description
You are given N words, one per line.
print a list of the words after removing any extra spaces.
Input
3
 cat
 dog
 fish
Output
['cat', 'dog', 'fish']
"""
n=int(input())
lst=[input().strip()for _ in range(n)]
print(lst)

"""
Problem 3 — Score Simulation
You will be given a number T (number of rounds).
Start with:
score = 0
Each round, you read an action name:
ADD → score += 3
BONUS → score *= 2
MISS → score -= 1
After all rounds, print the final score.
Input Example:
5
ADD
BONUS
MISS
ADD
BONUS
Output: 
16
"""
# Method 1
n=int(input())
lst=[input().strip()for _ in range(n)]
score = 0
for x in lst:
    if x == "ADD":
        score+=3
    elif x == "BONUS":
        score*=2
    elif x == "MISS":
        score-=1
    else:
        score+=0
print(score)

# Method 2
n=int(input())
score=0
for _ in range(n):
    x=input().strip()
    if x == "ADD":
        score+=3
    elif x == "BONUS":
        score*=2
    elif x == "MISS":
        score-=1
    else:
        score+=0
print(score)

"""
Problem 4 — Stop When Found (Hard – break)
You are given N animals, one per line.
Loop through the list and print each animal.
When you find "fish", print "Found fish!" and stop.
Input
5
cat
dog
bird
fish
cow

Expected Output
cat
dog
bird
Found fish!
"""
n= int(input())
lst=[input().strip() for _ in range(n)]
for x in lst:
    if x == "fish":
        print("Found fish!")
        break
    else:
        print(x)

"""
Part 5.2 — Multiple Lines (numbers)
Problem 1 — Sum of Numbers (Very Easy)
Problem
You are given an integer N.
The next N lines each contain one integer.
Find and print the sum of all the numbers.
Input
N
x1
x2
x3
...
xN
Output
The sum of the numbers
"""
# Method 1
n=int(input())
s=0
lst=[int(input()) for _ in range(n)]
for x in lst:
    s=s+x
print(s)

# Method 2
n= int(input())
s=0
for _ in range(n):
    x=int(input())
    s+=x
print(s)

"""
Problem 2 — Largest Number (Easy)
You are given an integer N followed by N integers, one per line.
Print the largest number.
Input
N
x1
x2
x3
...
xN
Output
The largest number
"""
n=int(input())
largest=float("-inf")
lst=[int(input()) for _  in range(n)]
for x in lst:
    if x>largest:
        largest=x
print(largest)

"""
Problem 3 — Count Positives (Easy)
You are given N integers, one per line.
Count how many of them are positive (greater than 0).
Input
N
x1
x2
x3
...
xN
Output
The number of positive integers
"""
n= int(input())
lst=[int (input()) for _ in range(n)]
count=0
for x in lst:
    if x>-1:
        count+=1
print(count)
