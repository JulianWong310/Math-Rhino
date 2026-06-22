"""
2026/01/09
Title: Draw an Hourglass Pattern
Problem Description:
Write a program to print an hourglass shape using asterisks (*).
Given a maximum width H (where H is an odd integer), the pattern
starts with H stars, decreases to 1 star, and then increases back to H stars.
Each line must be centered using leading spaces.

Example for H=5:
*****
 ***
  *
 ***
*****
"""
H=int(input())
for i in range(H,1,-2):
    star="*"*i
    space=" "*((H-i)//2)
    print(f"{space}{star}")
for i in range(1,H+2,2):
    star="*"*i
    space=" "*((H-i)//2)
    print(f"{space}{star}")