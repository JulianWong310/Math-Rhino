"""
2026-01-07
https://dmoj.ca/problem/ccc01j1
Your program should take as input the height H of the bow tie, where
H is an odd positive integer greater than or equal to 5. A bow tie with
H rows(2H columns) should then be printed using the pattern shown below in the sample output.

Input Specification
One line containing integer H
You may assume that all input data will be valid.

Sample Input 1
5

Sample Output 1

*        *
***    ***
**********
***    ***
*        *

Sample Input 2
7

Sample Output 2

*            *
***        ***
*****    *****
**************
*****    *****
***        ***
*            *
"""

H=int(input())
for i in range(1,H+1,2):
    star="*"*i
    space=" "*((H-i)*2)
    print(f"{star}{space}{star}")
for i in range(H-2,0,-2):
    star="*"*i
    space=" "*（(H-i)*2）
    print(f"{star}{space}{star}")