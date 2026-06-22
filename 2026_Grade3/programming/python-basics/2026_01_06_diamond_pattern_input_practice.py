"""
2026/02/06
Draw a Diamond (Rhombus) Pattern
Problem Description:
Write a program to print a diamond shape using asterisks (*).
Given a maximum width H (where H is an odd integer), the pattern
should increase from 1 star to H stars, and then decrease back to 1 star.
Each line must be centered using leading and trailing spaces.
"""
H=int(input())
for i in range(1,H+1,2):
    star="*"*i
    space=" "*((H-i)//2)
    print(f"{space}{star}{space}")
for i in range(H-2,0,-2):
    star="*"*i
    space=" "*((H-i)//2)
    print(f"{space}{star}{space}")