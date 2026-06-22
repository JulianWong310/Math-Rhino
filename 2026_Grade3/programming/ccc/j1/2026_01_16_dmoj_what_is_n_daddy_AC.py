"""
2026/01/16
https://dmoj.ca/problem/ccc10j1
"""
n=int(input())
count=0
for R in range(6):
    for L in range(6):
        if R+L==n and R>=L:
            count=count+1
print(count)