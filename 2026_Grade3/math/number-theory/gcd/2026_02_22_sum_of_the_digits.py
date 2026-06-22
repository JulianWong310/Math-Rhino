"""
Problem: Sum of Digits
You are given a positive integer N.
Your task is to compute the sum of its digits.
📥 Input
A single positive integer:
N
1
≤
𝑁
≤
10
18
1≤N≤10
18
📤 Output
Print a single integer: the sum of the digits of
𝑁
N.
🧾 Example 1
Input
47291
Output
23
Explanation:
4 + 7 + 2 + 9 + 1 = 23
🧾 Example 2
Input
100500
Output
6
Explanation:
1
 + 0 + 0 + 5 + 0 + 0 = 6
"""
# method 1
n=int(input())
bnm=0
while n>0:
    num=n%10
    n=n//10
    bnm=bnm+num
print(bnm)

# Method 2
print(sum(int(x) for x in input()))