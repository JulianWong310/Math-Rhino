"""
2026/01/27
Gauss 2016 Question 25
https://cemc.uwaterloo.ca/sites/default/files/documents/2024/2016Gauss7Contest.html
"""
# find the two closest divisors of 2016
min_diff=2016
for i in range(1,2017):
    if 2016%i==0:
        j=2016//i
        if j>=i and (j-i)<min_diff:
            min_diff=j-i
            min_i=i
            min_j=j
print(min_i,min_j)
print(min_i+min_j-1)

# find the closest divisors of input N
N=int(input())
min_diff=N
for i in range(1,N+1):
    if N%i==0:
        j=N//i
        if j>=i and (j-i)<min_diff:
            min_diff=j-i
            min_i=i
            min_j=j
print(min_i,min_j)
print(min_i+min_j-1)