"""
2026/02/10
https://dmoj.ca/problem/ccc17j2
"""
n=int(input())
k=int(input())
s=0
for i in range(k+1):
    s = s + n
    n = n * 10
print(s)