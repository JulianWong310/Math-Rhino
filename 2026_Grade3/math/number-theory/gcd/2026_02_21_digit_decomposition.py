# 2026/02/21

# Q1. Get 1, 2, 3, and 4 from the number 1234
x = 1234
a=x%10 # get 4
b=(x//10)%10 # get 3
c=(x//100)%10 # get 2
d=x//1000
print(a,b,c,d)

# Q2. The Mirror Number ChallengeTask:
# Given the integer x = 123, use only Floor Division (//) and Modulo (%) to extract each digit.
# Then, re-combine them to create the "Mirror Number" 321 and print the result.
x=123
a=x%10
b=(x//10)%10
c=x//100
print(a*100+b*10+c)

"""
Q3. Problem: Divisible by 9 (Digit Trick)
A number is divisible by 9 if the sum of its digits is divisible by 9.
You are given a three-digit integer N.
Task
Extract each digit.
Compute the sum of the digits.
Print True if the sum is divisible by 9, otherwise print False.
Input
A three-digit integer N.
Output
True or False
Example
Input
459
Output
True
"""
# Method 1
n=int(input())
a=n%10
b=(n//10)%10
c=n//100
cnt=a+b+c
print(cnt%9==0)

# Method 2
n=input().strip()
cnt=0
for x in n:
    cnt+=int(x)
print(cnt%9==0)

