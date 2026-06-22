"""
2026/02/21
Topic: Divisibility & Remainders
"""
"""
Problem 1 — Cupcake Boxes
A bakery packs cupcakes into boxes.
Each box can hold 8 cupcakes.
You are given an integer n, representing the total number of cupcakes.
Task
Determine how many cupcakes will be left over after filling as many full boxes as possible.
Input
A single integer n.
Output
A single integer representing the number of leftover cupcakes.
Example
Input
250
Output
2
"""
n=int(input())
print(n%8)

"""
Problem 2 — Tournament Groups
In a tournament, players are divided into groups of 4.
You are given an integer P, representing the total number of players.
Task
Print:
The number of full groups.
The number of players who cannot be placed in a full group.
Input
A single integer p.
Output
Two integers on separate lines:
Number of full groups
Number of leftover players
Example
Input
22
Output
5
2
"""
p=int(input())
print(p//4)
print(p%4)

"""
Problem 3 — Potential Leap Year
A year is considered a potential leap year if it is divisible by 4.
You are given an integer Y, representing a year.
Task
Print True if the year is divisible by 4
Otherwise, print False.
Input
A single integer Y.
Output
True or False
Example
Input
2026
Output
False
"""
Y=int(input())
print(Y%4 == 0)

"""
Problem 4 — Lucky Seven
You are given an integer N.
Task
Print True if:
N is an integer, AND
N is divisible by 7
Otherwise, print False.
Input
A single value N.
Output
True or False
Example
Input
49
Output
True
"""
n=int(input())
print(n%7==0)

"""
Problem 5: Day After Many Days
In this problem, we represent the days of the week using integers from 0 to 6:
Number	Day
0	Sunday
1	Monday
2	Tuesday
3	Wednesday
4	Thursday
5	Friday
6	Saturday
You are given:
An integer D representing today's day.
An integer N representing the number of days that pass.
Your task is to determine what day it will be after N days.
Input
Two integers:
D
N
0 ≤ D ≤ 6
0 ≤ N ≤ 10^9
Output
Print a single integer representing the day of the week after N days.
Example 1
Input
5
30
Output
0
Example 2
Input
1
14
Output
1
"""
D=int(input())
N=int(input())
print((D+N)%7)
