"""
2026/01/10
Problem of the Week
Source: University of Waterloo - CEMC Problem of the Week (POTW)
Problem: Beaded Bracelets
Aditi and Ersal have designed a bracelet that has 17 beads.
The bracelet has a red beads, b green beads, and the rest of the beads are yellow.
(a) How many yellow beads are in one bracelet?
(b) They want to make a total of N bracelets, so that everyone in their class can have one.
Each package of beads contains 24 beads:
8 red beads
8 green beads
8 yellow beads
How many packages of beads do they need to make all the bracelets?
first line,
red beads: a (a<=17)
second line
green beads: (b<=17)
third line: N bracelets
input
6
9
7
output
6
input
6
9
21
output
24
"""
a=int(input())
b=int(input())
n=int(input())
c=17-(a+b)
if a>=b and a>=c:
    L=a
elif b>=a and b>=c:
    L=b
else:
    L=c
p=L*n
if p%8==0:
    print(p/8)
else:
    print(p//8+1)